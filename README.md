The live link to Sweet Freeze Ice Cream bar can be found here - <https://sweet-freeze-dfb3ab7b2174.herokuapp.com/>

# Sweet Freeze 
Is an ice cream bar in my town that sell assorted ice cream flavour all year round.
I'm building a data automation to help their staff pre-make stock to sell by collecting the company's daily data worksheet in other to calculate their sales and and surplus so they will know how many ice cream they will produce the next business day.

## Features

### Existing Features
There is google sheet with data to work with. The google sheet contains both the sales data worksheet, leftover data and stock data worksheet. And this data is being updated any time user enters new data and the data.
The leftover data has both positive and negative number. The negative numbers are leftover ice cream that was thrown away while the positive numbers are extra ice cream made when the stock ran out.
Each time we enter new data the worksheet is updataed with the new data and in other for the worksheet to update each time user enter new data, API was used. API allows different applications to share data. I set up API which allows my python project to access and updata data in the spreadsheet. 

### Features Left to Implement

## Testing

I have tested this project code by:
  . Pasting the code on PEP8 linter and there were no error found. [PEP8 Python Validation](https://pep8ci.herokuapp.com/)
  . I have added both valid and invalid data while runing the code on App.codeanyway and it printed correctly when valid data was applied and incorrect when invalid data was appiled. When invalid data is entered, it tells users the data entered is invalid and what data user should enter "Data should be twelve numbers, separated by commas.
  . The code was also tested after deployment on Code Institute Heroku terminal and it run successfully and the google worksheet was updated each time I enter a new data

## Bugs
## Solved Bugs
   . After adding and calculated my stock data it was not refecting on the worksheet as it should. This was fixed by updating the stock data on the main function

## Remaining Bugs
    . No bugs remaing and no warning either.

## Validator Testing
    . No errors were returned from PEP8online.com    

## Deployment

This project was deployed using Code Institute's mock terminal fro Heroku. and the steps for deployment are as followed:
### First step
  . Sign in to Heroku app
  . Create a new app with a unique name
  . Go to setting and create a _Config Var_ called `PORT`. Set the value to `8000`
  . Add another _Config Var_ called `CREDS` and here I added my `creds.json` file.
  . Then click on  buildpacks and add the following:
1. `heroku/python`
2. `heroku/nodejs`
### Second step
  Click on deploy at the top left side and select github to connect to github. Confirm and search for the github repositery name, click connect to link up the Heroku app we creacted ealier with the repositery.
  . Choose either automatic deploy or manual. I used manual which is deploy branch.
  . Allow the app to build until it shows successfully then click view and it takes me to my deployed link.


Credits 
   . Anna Graves for love sandwitches walthrough project
Sweet Freeze data entery was built with knowlege from love sandwitches walkthrough project created by Anna Graves.
   . Code Institute for the deployment terminal