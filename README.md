<!-- Project Head -->
<br />
<div align="center">
  <a href="https://github.com/po-the-panda-12/Battlebots">
    <img src="BWP.jpg" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">Battlebots</h3>

  <p align="center">
    Battlebots match prediction based on pre-interview scripts
    <br/>
  </p>
</div>

</br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project first extracts the text from the pre-interview video and uses nlp to predict win or lose.

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com) -->

<!-- Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

(For Python) <br/>
This is an example of how to list things you need to use the software and how to install them.
* tensorflow
  ```sh
  pip install tensorflow
  ```
* pandas
  ```sh
  pip install pandas
  ```
* pytesseract
  ```sh
  pip install pytesseract
  ```
* Pillow
  ```sh
  pip install Pillow
  ```

### Installation

<!-- 1. Get a free API Key at [https://example.com](https://example.com) -->
1. Clone the repo
   ```sh
   git clone https://github.com/po-the-panda-12/Battlebots
   ```
  
2. Run program
   ```sh
   python3 nlp.py 
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The purpose of using pre-interview scripts for match prediction is to highlight how words have power. It reflects the player's mindframe and simple negative phrases like "we can't do this" or "we won't win if we don't..." lead them to the losing side.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- Pre-interview script extraction
  - vid_extract.py - uses ocr to generate video to script text
 
- Match prediction 
  - nlp.py - predicts match outcome based on scripts


<p align="right">(<a href="#top">back to top</a>)</p>

