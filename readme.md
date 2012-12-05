# AGRC SGID SDE Connection/Usability Timer #

---
**Must** have python **2.5** or higher and ArcGIS **10.0** or higher.

I am writing to request a favor. We are having some performance issues with folks using SDE connections that we believe may be related to how the new state fire wall is configured.

I am hoping that you might be willing to set up and run a python script that will generate performance metrics for both our 93 and 10 servers.

Here's how to do it.

1. **Click** [ZIP](https://github.com/agrc/SdeTimer/archive/master.zip) to download the source code from our github repository.

2. **Find** the downloaded zip file (named `SdeTimer-master.zip`) in its download folder and **extract/unzip** the file to the location of your choice. By default, the contents will extract to a folder named `SdeTimer-master`.

3. **Take** the [broadband speed test](http://www.utah.gov/broadband/address.html?type=test) and note your **download** speed in Mbps.

4. In the extracted `SdeTimer-master` folder, **right click** on `SgidConnectionTimes.py` and open it in a text editor or a python editor. **Modify** lines `14` and `15` to be specific for your _location_ and _connection speed_

- **Find** testLocation = `'AGRC Office'` and change the value in single quotes to a description of your location (ex. `DEQ HSandbeck desktop`)
- **Find** testDownloadMbps = `'100 Mb'` and change the value to your speed (ex. '18 Mb')
- **Save** your file and **exit**.

5. In the extracted SdeTimer-master folder, **double click** the `install.bat` file to **install** the Google Drive python library needed to write results to our google spreadsheet that contains the results.

6. **Double click** on the `SgidConnectionTimes.py` file to run the script. A Command window will open and may run in the background for anywhere between **1** to **30 minutes**. This process will get a list of all feature classes and will time the reading of 1,000, 100,000, and the full record set (387,000 features) from the `SGIDxx.Transportation.Roads` dataset. It will do this for our 93 and 10 SDE servers. When it's **done**, the CMD window will **close** and the results will be sent to the google spreadsheet.

Thanks,

AGRC