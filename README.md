# GSoC Organization Filter (2018)
Idea credit - [Rohith ASRK](https://github.com/rohithasrk/GSoC-Organisation-Scraper)

This is a simple web scraping Python script (package used - BeautifulSoup) made to make your GSOC recon easier, as going through every organization and checking the programming languages/technologies involved is a bit of a tiring task.

### I. How to use it
The usage is pretty straightforward. Just go to this [link](https://neuralflux.github.io/gsoc-organization-filter/) (hosted via GitHub Pages).

Use the search bar to search for the organization, technology or topic, all in one place.

### II. Contribution
#### A) To Python script
1. Open a PR with an apt heading and description of what has been improved.
2. If this change affects the produced HTML too, follow part B of this section as well.

#### B) To HTML file
1. Any changes to the HTML can be only made to the search box, table or JavaScript.
2. Upload demo on JSFiddle, CodePen or any other website which achieves the purpose.
3. In the PR, mention what has been improved and also give the link to the aforementioned demo.

### III. How to run
1. Install all the packages required by `pip install -r requirements.txt`
2. Download both the python scripts and HTML if necessary.
3. Run the `gsoc_filter_by_languages_or_topics.py` and it will produce an HTML output.

### IV. To-Do
- [ ] Escape , (commas) in organization names
- [ ] Enumerate number of years participated for each Organization
