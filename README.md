# Shopping List Manager #

* The shopping cart manager is an direct equivalent to the popular shopping list manager program, It is a kind of shopping bot that allows the user input and manipulation of data according to the user choices and the shopping bot outputs a result based on user choices and input.

* The aim of this program is to help user have a proper planning with grocery shopping, by having a grocery list is beneficial to a user in a lot of ways.
    First, a user will likely make an improptu decision to impulse buy a product that was never in the plan, this kind of uncontrolled urge will definitly impact the user financially, which the ripple effect can spread all the way to incur debt , which can eventually be a detriment to a once healthy credit score. However, having a proper planning of the items you want to buy could come in handy as it will help in avoiding over spending, and impulse buying by helping user to focus on what is really needed.

* Secondly, the shopping list program saves user time and energy, not having a list of what to buy at the store makings shopping a headache and time consuming as wider product choices can be a distraction which can be overwhelming sometimes, but if you already have the choice of items you which to buy makes shopping very easy and less time consuming. In the same vein, having a shopping list reduces waste in the sense that when you buy things you do not really need immediatly it most times end up in the trash.

* Further more, it can help in improving user memory and helps user to focus and have proper planning of things.

![title and logo screen](/images/title.png)

## Features
_______________________________

### Greeting

*  The first thing a user sees when the program is been executed is a display of the program title with a design.

* It asks the user to input a name which is then displayed as a greeting.


![greeting](/images/greetings.png)


### Option Menu 
* This is a section the shows  to the user available option to selct from. 

* This option ranges from 1 to 7.

* Based on user selection the program execute each task accordingly.
	


![Option Menu](/images/optionmenu.png)

#### Option 1: Add item to list.

* This option allow user to add items to the list.
* It also tells the user if an item has already been added to avoid repetition.


![object selection section](assets/images/optionarea.png)
![object selection section](assets/images/optionarea.png)

#### Option 2: View List

* This option displays the content of the list. 

* If nothing was previously added it displays "List is empty, try adding adding an item".

![Footer section](assets/images/gameplay.png)
![Footer section](assets/images/gameplay.png)


#### Option 3: Total number of items in the list

* This option displays the total number of items on the list. 

* Displays "0" if the list is empty


![score section](assets/images/playerscore.png)

#### Option 4: Find items in the list
	
* The find item in the list option searches the list for a user specified item name, which then search and returns a message if the item is found or not 


![Footer section](assets/images/rules.png)
![Footer section](assets/images/rules.png)


#### Option 5: Delete items from the list

* The delete item from the list option also searches the list for a user specified item name, which then search and delete the item if found on the list or not.


![Footer section](assets/images/rules.png)
![Footer section](assets/images/rules.png)


#### Option 6: Empty  the list

* This erase every content of the list and return it back to an empty list.
* It prints a message based on if the list is already empty or not.

![Footer section](assets/images/rules.png)
![Footer section](assets/images/rules.png)

#### Option 7: Exit program

* This function allows user to exit the program.
* It gives the user an option to chose either to exit or run the program again from the beginning.
* It also print a thank you message to the user based on the time of the day.

![Footer section](assets/images/rules.png)

## Testing

* This program was properly tested using Pep8 online [Pep8](https://www.http://pep8online.com/checkresult "pep8") .

* All the generated errors like "trailing white spaces and no newline at the end of file were rectified.

* I confirm that all the functionality of this program works perfectly.

![Footer section](/images/pep8.png)
## Tools used

### Language
* Python

### Other program used: 
* Gitpod:
    * Gitpod: A versatile IDE used to code the program [Gitpod](https://www.gitpod.io/ "gitpod")

* Github:
    * Github: a platform used for storing, tracking, and collaborating on software projects  [Github](https://www.github.com/ "github")

* Git:
    * Git: Used for version control.

* Pep8:
    * pep8: an online python code checker  [pep8](https://http://pep8online.com/checkresult/ "pep8")

* Heroku:
    * Heroku: used in the deployement of the program  [Heroku](https://http://heroku.com/ "Heroku")



## Bugs
* No bugs was found as at the time of deployment.


##  User Input Validation.

* User input validation
	* The program code was written in a way that it controls any invalid user data input, It allows inputs like "Peanut butter", "Scottish- Whiskey". The error messages were controlled by use of various conditional statements.

## Deployment

* The program was deployed to Heroku by following this steps.

* On the Heroku wesbite, create an account.

* After signing in into your account click on create new app button.

* Chose a unique name for the application to be deployed.

* Chose a region.

* Click on settings.

* Navigate to Config var.

* In the Key Value space we need to input PORT for KEY must be in capitals and 800 for PORT

* Click add.

* Click add buildpack, choose python first save changes and add nodjs must be in this order.

* Navigate to the deploy tab on the menu.

* Chose your choice of deployment github is the choice for this project.

* Enter your github repository name and search, if found then click connect.

* Chose to either deploy automatically or manually.

* On this project, our choice is manual deployment, click and wait until a message appear confirming that the application was successfully deployed.

* Click on view app button to run the application.


* The Live link to the deployed program is  [Shopping list](https://gullah26.github.io/Rock_Paper_Scissors/ "rock paper scissors").

## Credits

* Content

	* The part of the code to make the function check winner was from  [sebhastian](https://sebhastian.com/rock-paper-scissors-javascript/ "sebhastian")

	* The inspiration to start  the project is from  Code Institute Portfolio Project Scope.


## Media

* The Images used on this game  was taken from [png set](https://pngset.com/download-free-png-yiceg "png set").
