# Wiwino Data Analysis

## Used libraries (no venv on this one, you'll be fine...)
- sqlite3
- pandas

## Usage
Open `analysis.ipynb` and run the first cell to connect to the database and print an overview. Table info will also be saved to table_info.txt.

## Analysis
### Ratings overview: 10 most profitable wines?
The first thing to notice is that the (non-zero) ratings of both vintages and wines are not that varied. All values lie between 4.1 and 4.9 and can be considered to be decent enough. It is therefore important to consider the count as well. We should of course also include the price in the equation.

Current (fairly arbitrary) equation goes as follows:
`Rating * LOG(Count * 0.1 + 2.2)`
This equation makes sure that low popularity results in a very low or even negative score.