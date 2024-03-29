# Wiwino Data Analysis

## Used libraries (no venv on this one, you'll be fine...)
- sqlite3
- pandas

## Usage
Open `analysis.ipynb` and run the first cell to connect to the database and print an overview. Table info will also be saved to table_info.txt.

## Analysis
### 1. Ratings overview: 10 most profitable wines?
The first thing to notice is that the (non-zero) ratings of both vintages and wines are not that varied. It is therefore important to consider the count as well. We should of course also include the price in the equation.

Current (fairly arbitrary) equation goes as follows:
`Rating * LOG(Count * 0.001 - 3)`
This equation makes sure that low ratings count results in a very low or even negative score.
So it is better to have a lower price, and even a lower rating, but high popularity than the other way around.

### 2. Marketing budget: which country?
Let's see... Most users per country seems like a good approach, but most users per winery per country seems even better. What better country to sell to than one that loves drinking wine more than producing it.

### 3. Three Relevant Wineries
Wrongly encoded information is keeping us from knowing the names of the wineries involved... Luckily it would appear that the vintage name contains the winery name, and we can extract it using SUBSTR()

Let's select wineries that have vintages where the year is not missing and have been at least active since 2010, also let's ignore vintages whithout any ratings.
Let's keep track of each winery's best rating and the total ratings count.

We order by this fancy score again but slightly different, it is a bit more sensitive to the rating than in previous queries: `Rating * LOG(Count * 0.000001 + 1.5)`

Increase the count multiplier to make the score more sensitive to the count instead.

### 4. Coffee, Toast, Cream, Green Apple and Citrus
Check out that beautiful list of Champagne tasting wines...

### 5. TOP 5 Wines for the TOP 3 Grapes
Let's just go by ratings...

### 6. Wine and vintage leaderboard for each country
Got no visuals, my bad.

### 7. TOP 5 Cabernet Sauvignon pour Monsieur Vielle-Pie
One of our VIP clients likes Cabernet Sauvignon, let's give him what he wants.
