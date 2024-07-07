# Immfly-test

**We would love to see your Selenium and Python skills in action. Can you automate the case to detect if the products are ordered correctly by name or by price?**


The automated cases have been done using playwright and phyton.
The test cases in questions tests the following behaviours:
 - The sorting arrow shows the selected options
 - The products are sorted correcly while being in default status
 - The sorting by product name and product price in both ascending and ascending order are working correctly.

The solution that I have found (and I know is not the most optimal one) is sorting the elements and assert that the expected one is visible and assert that a non expected one is not visible.

**How to run the tests:**

**From the pipeline** - Go to Actions and run the last worflow "Test this workflow"
![Screenshot 2024-07-07 at 14 17 28](https://github.com/Albertofly/Immfly-test/assets/174526111/00a6312e-df01-483c-939c-27959fb1820c)
![Screenshot 2024-07-07 at 14 18 10](https://github.com/Albertofly/Immfly-test/assets/174526111/9b0fd64b-e6de-45ad-91a1-453dd09899ab)

**Locally** - Clone the project (make sure you have all the dependencies and IDE)
**Different modes of running the tests:**

- **run the tests**- pytest

- **run the tests opening browser (configured only for chrome)**- pytest --headed

- **run the tests only for acceptance criteria**- pytest -m acceptance_tests

- **run the tests parallel mode**- pytest -n6

- **run the tests generating an html report**- pytest --template=html1/index.html --report=acceptance_test_report.html

![Screenshot 2024-07-07 at 14 19 30](https://github.com/Albertofly/Immfly-test/assets/174526111/2353b3cd-0da3-4022-844d-fa8677bbcf78)

![Screenshot 2024-07-07 at 14 19 53](https://github.com/Albertofly/Immfly-test/assets/174526111/62f5a7b8-a0f4-45bc-88b9-0feb6449eadc)

