The live link to Sweet Freeze Ice Cream bar acn be found here - <https://sweet-freeze-dfb3ab7b2174.herokuapp.com/>

# Sweet Freeze 
Is an ice cream bar in my town that sell assorted ice cream flavour all year round.
I'm building a data automation to help their staff pre-make stock to sell by collecting the company's daily data worksheet in other to calculate their sales and and surplus so they will know how many ice cream they will produce the next business day.

## Features

### Existing Features
There is google sheet with data to work it. The google sheet contains both the weekly sales data, left over and stock data worksheet.
The leftover data has both positive and negative number. The negative numbers are leftover that was thrown away while the positive numbers are extra ice cream made when the stock ran out.
Each time we enter new data the worksheet is updataed with the new data

### Features Left to Implement

## Testing

I have tested this project code by:
  . Pasting the code on PEP8 linter and there were no error found
  . Add both valid and invalid data while runing the code on App.codeanyway and it printed correctly when valid data was applied and incorrect when invalid data was appiled
  . The code was also test after deployment on Code Institute Heroku terminal and it run successfully
  [PEP8 Python Validation](https://pep8ci.herokuapp.com/)

## Bugs
## Solved Bugs
   . After add and calculating my stock data it was not refecting on the worksheet as it should. This was fixed by updating the stock data on the main function

## Remaining Bugs
    . No bugs remaing and no warning either.

## Deployment

This project was deployed using Code Institute's mock terminal fro Heroku. and the steps for deployment are as followed:
  . Sign in to Heroku app
  . Create a new app with a unique name
  . Go to setting and create a _Config Var_ called `PORT`. Set this to `8000`
  . Another _Config Var_ called `CREDS` where I added my `creds.json` file.
  . Then click on  buildpacks and add the following:

1. `heroku/python`
2. `heroku/nodejs`
### Second step
  Click on deploy and select github to connect to github. Confirm and search for the github repositery name, click connect to like up Heroku app we creacted ealier.
  . Choose either automatic deploy or manual. I used manual which is deploy branch.
  . Allow the app to build until it shows successfully then click view and it takes me to my deployed link.


Credits 
   . Anna Graves for love sandwitches walthrough project
Sweet Freeze data entery was built with knowlege from love sandwitches walkthrough project created by Anna Graves.
    . Code Institute for the deployment terminal