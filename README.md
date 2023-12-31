The live link to Sweet Freeze Ice-Cream bar can be found here - <https://sweet-freeze-dfb3ab7b2174.herokuapp.com/>
# Sweet Freeze 
Is a python game which runs in the Code Institute mock terminal on Heroku. It is an ice-cream bar in my town that sell assorted ice-cream flavour all year round.![Responsive Mockup](readme/amiresponsive.png)
I created a data automation to help their staff pre-make stock to sell by collecting the company's daily data worksheet in other to calculate their sales and and surplus so they will know how many ice-cream they will produce the next business day. ![Data automation](readme/sweetfreeze-data-automation.png)

## Features

### Existing Features
    . There is google sheet with data to work with. The google sheet contains both the sales data worksheet,
    leftover data and stock data. And this worksheet is being updated any time user enters new data.
    . The leftover data has both positive and negative number. The negative numbers are leftover ice-cream while the positive numbers are extra ice-cream made when the stock ran out.
    . Each time we enter new data the worksheet is updataed with the new data and in other for the worksheet to update each time user enter new data, API was used. API allows different applications to share data. I set up API which allows my python project to access and updata data in the spreadsheet. 
![Googel spreadsheet](readme/google-spreadsheet.png) 

### Features Left to Implement
    . Make the app to show what's in the spreadsheet. The spreadsheet contains dailysales, leftover and stock data. which should show on the app screen.
    . Give users the ability choose what they want to do for example Hello user, what do you want to do today? Then an option to choose if the user want to view data or to input data or see the leftover data.

## Testing

I have tested this project code by:
    . Pasting the code on PEP8 linter and there were no error found. ![PEP8 Python Validation](readme/python-validation.png)
    . Tested after deployment on Code Institute Heroku terminal and it run successfully and the google worksheet was updated each time I enter a new data.
    . I have tested both valid and invalid data ![Tested with invalid data](readme/invalid-data.png). When invalid data is entered, it tells users the data entered is invalid and tells user what data to enter "Data should be twelve numbers, separated by commas. ![Enter data](readme/enter-data.png)

## Bugs
## Solved Bugs
    . After adding and calculated my stock data it was not updating on the worksheet as it should. This was fixed by updating the stock data on the main function

## Remaining Bugs
    . No bugs remaing and no warning either.

## Validator Testing
    . No errors were returned from PEP8online.com
    [PEP8 Python Validation]<https://pep8ci.herokuapp.com/>    

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku and the steps for deployment are as followed:
### First step
    . Sign in to Heroku app
    . Create a new app with a unique name
    . Go to setting and create a _Config Var_ called `PORT`. Set the value to `8000`
    . Add another _Config Var_ called `CREDS` and here I added my `creds.json` file.
    . Then click on  buildpacks and add the following:
1. `heroku/python`
2. `heroku/nodejs`
### Second step
  Click on deploy at the top left side and select github to connect to github. Confirm your connection to github and search for the github repository name, click connect to link up the Heroku app creacted ealier with the repository.
    . Choose either automatic deploy or manual. I used manual which is deploy branch.
    . Allow the app to build until it shows successfully then click view and it takes me to my deployed link.


Credits 
    . Anna Graves for love sandwitches walthrough project
Sweet Freeze data entery was built with knowledge from love sandwitches walkthrough project created by Anna Graves.
    . Code Institute for the deployment terminal