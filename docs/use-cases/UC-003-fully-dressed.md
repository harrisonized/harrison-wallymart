Use Case 003: Customer Orders a Product

| Name                  | UC-003: Customer Orders a Product                            |
| --------------------- | ------------------------------------------------------------ |
| Scope                 | System Use Case                                              |
| Level                 | System Goal Level                                            |
| Primary Actor         | Customer                                                     |
| Stakeholder(s)        | AmazingCo will be providing the Wallymart App to customers and employees. |
| Preconditions         | The user must download the software from Github and have Python installed. |
| Postconditions        | The orders table is updated with the customer’s orders.      |
| Main Success Scenario | 1. The customer starts the app.<br />2. The app creates any missing database-tables.<br />3. The customer is prompted to sign up or log in. <br />4. The customer logs in by entering his username and password.<br />5. The app checks the customer_credentials table for the customer’s username and password combination and then authenticates the user.<br />6. From the customer home page, he is prompted to choose one: (1) view products, (2) checkout, (3) update profile, or (4) log out. <br /> 7. The customer chooses to view products. He is shown the first five items and prompted with the following options: (1) refresh products, (2) next page, (3) previous page, (4) add item to cart, (5) write a review, (6), view reviews, or go back to the home screen.<br />8. The customer selects next twice, then decides to add 3 of item number 12 to his cart. He selects previous page and adds 5 of item number 6 to his shopping cart. <br />9. The customer returns to the home page and selects checkout.<br />10. The customer sees the contents of the shopping cart and decides to submit his order. <br />11. The app prompts the customer for credit card information, which he enters. The app verifies it and writes the order to the orders table. <br />12. The customer logs out. |
| Extensions            | 1a1. The customer enters his credentials incorrectly.<br />1a2. The app checks the customer_credentials table for the customer’s username and password combination and cannot find it.<br />1a3. The customer sees the following message: “Please enter a valid username and password combination.” <br />1a4. The customer is re-prompted for his username and password.<br /><br />2a1. The customer logs in and immediately decides to check out, despite having no items in his cart.<br />2a2. The customer sees the following message: “No items in cart, returning to home...” |


 
