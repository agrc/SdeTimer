# download http://code.google.com/p/gdata-python-client/downloads/detail?name=gdata-2.0.17.zip
# extract files from zip
# from extracted folder, run 'setup.py install'
# modify test location to be where you are
# modify testDownloadMbps to be your connection speed

import os
import time
import arcpy
import gdata.spreadsheet.service
from datetime import datetime, timedelta

class SdeTimer(object):
	testLocation = 'AGRC Office'
	testDownloadMbps = '100 Mb'
	server = ''
	connectionString = ''
	values = {}
	layer = ''

	def __init__(self,version):
		self._setupSdeVersion(version)
		self.values['date'] = time.strftime('%m/%d/%Y %H:%M:%S')

		self.values['testlocation'] = self.testLocation
		self.values['server'] = self.server
		self.values['testdownloadspeed'] = self.testDownloadMbps

	def _setupSdeVersion(self, version):
		version = str(version)
		self.server = 'SGID' + version
		self.connectionString = r'agrc@SGID{0}@gdb{0}.agrc.utah.gov.sde'.format(version)
		self.layer = os.path.join(self.connectionString, "{0}.Transportation.Roads".format(self.server))

	def TimeToListRows(self):
		print "Timing feature querying."

		count = 0

		sc = None
		sc = arcpy.SearchCursor(self.layer,"")

		starttime = datetime.now()

		try:
			for row in sc:
			    count = count + 1
			    if count == 1000:
			        endtime1K = datetime.now()
			    elif count == 100000:
			        endtime100K = datetime.now()
		finally:
			if sc:
				del sc

		endtime = datetime.now()

		print "All records iterated."

		self.values['time100krecords'] = str(self.ToMilliseconds(starttime, endtime100K))
		self.values['time1krecords'] = str(self.ToMilliseconds(starttime, endtime1K))
		self.values['timeallrecords'] = str(self.ToMilliseconds(starttime, endtime))
		self.values['countallrecords'] = str(count)

		print "1000 records: {0} {1}".format(self.values['time1krecords'],'milliseconds.')
		print "100000 records: {0} {1}".format(self.values['time100krecords'],'milliseconds.')
		print "{0} records: {1} {2}".format(count, self.values['timeallrecords'], 'milliseconds.')

	def TimeToListSdeCatalog(self):
		print "Timing the list of SDE layers..."
		starttime = datetime.now()

		arcpy.env.workspace = self.connectionString
		f = arcpy.ListFiles()

		endtime = datetime.now()

		self.values['timegetcatalog'] = str(self.ToMilliseconds(starttime, endtime))

		print "Done. {0} {1}".format(self.values['timegetcatalog'],'milliseconds.')

	def ToMilliseconds(self, start, stop):
		offset = stop - start
		return (offset.days * 24 * 60 * 60 + offset.seconds) * 1000 + offset.microseconds / 1000.0

	def LogToGoogle(self):
		print "Sending speed data to google spreadsheet."

		email = 'agrctest@gmail.com'
		password = 'PASSWORD HERE'

		spreadsheet_key = '0Al_OtOSAbDs7dFRMZzBpMWpfZExlZnhoTHRDbmktcnc'
		worksheet_id = 'od6'

		spr_client = gdata.spreadsheet.service.SpreadsheetsService()
		spr_client.email = email
		spr_client.password = password
		spr_client.source = 'SGID Connection Tests'
		spr_client.ProgrammaticLogin()

		entry = spr_client.InsertRow(self.values, spreadsheet_key, worksheet_id)

		if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
		  print "Your speed test was logged."
		else:
		  print "Your speed test failed."

	def Start(self):
		self.TimeToListSdeCatalog()
		self.TimeToListRows()
		self.LogToGoogle()

timer = SdeTimer(10)
timer.Start()

timer = SdeTimer(93)
timer.Start()
