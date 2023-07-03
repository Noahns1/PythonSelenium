# PythonSelenium

---
### :man_technologist: About me:
I have a strong background in Quality Assurance and automation, and I am equally passionate about software development. Additionally, I have received comprehensive training in Java full-stack development, and I possess proficient programming skills in Python.

[LinkedIn](https://www.linkedin.com/in/noah-schlaupitz-786a04195/)

---
Languages and Tools:
<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/selenium/selenium-original.svg" width="40" height="40"/>&nbsp;
  <img src="https://camo.githubusercontent.com/9afcdb94ede677a8c791beaa5031755af94ac56969bedd3b3e9af9b48d535fa5/68747470733a2f2f7261772e6769746875622e636f6d2f6265686176652f6265686176652f6d61737465722f646f63732f5f7374617469632f6265686176655f6c6f676f312e706e67" width="40" height="40"/>&nbsp;
</div>

---
### What Is My Project?
This project is part of a twin set of projects that achieve identical functionality. In this project, Python, Selenium, and Behave are utilized for Behavior-driven development (BDD) to automate test cases on Amazon. Its twin project achieves the same test cases but implements Java, Maven, Selenium, TestNG, and Cucumber.

[Twin Project](https://github.com/Noahns1/JavaSelenium)

---
### Why Is This Project Useful?
I developed this project to showcase not only my proficiency in test case creation and automation but also demonstrate my adeptness in both Python and Java. Regardless of the language used, the project accomplishes the same functionality, highlighting my versatility and understanding of different programming languages.

---
### Dependencies
- Selenium webdriver
- Behave

---
### How To Use This Project

1. Update the Chrome webdriver location in "context.driver=webdriver.Chrome()"
2. Ensure all dependencies are downloaded and installed
3. To run a feature file run this command in project terminal "python -m behave folder\file.type"
    - Example: python -m behave features\amazon.feature 
4. To run a specific scenario run this command in project terminal "python -m behave -n "scenarioName"
    - Example: python -m behave -n "Amazon - Incorrectly attempt to create an account"

---
### Scenarios
In this project, I have implemented three scenarios that are identical to those in the twin project. The only difference is that they have been converted to Java.

These Scenarios are:

1. Test drive webdriver
     - This is a "test drive" scenario to validate the functionality of Behave and Selenium installations.
2. Amazon - Find Selenium book and add to cart
     - This scenario focuses on searching for an item, selecting it, adding it to the cart, and then validating its presence in the cart.
3. Amazon - Incorrectly attempt to create an account
     - This scenario concentrates on negative testing by simulating errors that arise when incorrect input information is provided for creating an account.

