# QrSorter
App for sorting packages based on their QR codes with a web app that displays the results.

## Technologies
* Python 3
* ASP.NET Core in .NET 5
* SQLite
* JavaScript
* CSS3
* HTML5

## Setup
To run this project first install packages from requirements.txt:
```
pip install -r requirements.txt
```

When packages are installed simply execute ```main.py```, this will start the conveyer belt:
```
python QrSorterApp/main.py
```

To publish and run web app execute the following commands:
```
cd YourPath/QrSorterUI
dotnet publish -c Release -r linux-arm --output ./MyTargetFolder QrSorterUI.sln
```

If you haven't run previous commands on your Raspberry Pi then transfer MyTargetFolder to it. 
Next run the following commands:

```
cd /MyTargetFolder
chmod +x QrSorterUI
./QrSorterUI
```

Server should start on port 54321.

If the database doesn't exist then first run ```main.py``` to create it.

## Construction
Conveyer belt was built using:
* Raspberry Pi
* webcam
* phototransistor
* two servomechanisms
* stepper motor
* laser diode
* LEGO pieces

![Alt Text](https://github.com/DawidMichalak/QrSorter/blob/main/images/construction.jpg)

![Alt Text](https://github.com/DawidMichalak/QrSorter/blob/main/images/ConveyerBelt.gif)
