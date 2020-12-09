<!-- ABOUT THE PROJECT -->
## About The Project

Python program that scrapes Amazon price data and alerts the user through email if their speicifed item's price falls. <br />
In 2020, Amazon updated their site and the Requests + BeautifulSoup libraries no longer work for scraping site data.
However, the Requests-HTML library was one of the methods that I found to work as of December 2020. 


### Built With

* Python
* Requests-HTML Library
* smtplib Library



<!-- GETTING STARTED -->
## Getting Started

To get a local copy running follow these steps.

### Prerequisites

Install Requests-HTML library
  ```sh
  pip install requests-html
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```

<br />
After installation, find URL of the desired Amazon product, and store it in URL variable. Also change sender/reciever email as needed.

<!-- USAGE EXAMPLES -->
## Usage

Program will continue to scan the desired product every 10 minutes, outputting the time and the title/current price of the item. 

<img width="582" alt="Screen Shot 2020-12-09 at 12 53 14 PM" src="https://user-images.githubusercontent.com/69620469/101686449-ed062e80-3a1d-11eb-8a42-b5d8fde8dd15.png">

Once it detects that the item has decreased in price, it will stop running and give an alert that an email has been sent. 

<img width="576" alt="Screen Shot 2020-12-08 at 8 36 53 PM" src="https://user-images.githubusercontent.com/69620469/101585938-a836b500-3995-11eb-9e06-736057b73e53.png">

The email sent to the user will contain the link to their desired product.

<img width="1410" alt="Screen Shot 2020-12-08 at 8 38 03 PM" src="https://user-images.githubusercontent.com/69620469/101686319-be885380-3a1d-11eb-9379-7e7cfb70be4e.png">





<!-- CONTACT -->
## Contact

Max Li - maxli9132@gmail.com
