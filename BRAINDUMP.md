Bad workaround for mass-input

1. So I have five files I wanted to mass process, and I didn't want to freaking change the input in the script every single time for each
2. So, I had an array listing the file names, and then I wrapped the entire processor within a forEach loop of the array, running the script per item
3. The issue, however, IS THE CATEGORY COUNTS
  3.1. The problem:
    3.1.1. I assumed, initially, when I built this script, that all CSV results from the APIFY scraper will have a set number of category columns, namely 10 from 'categories/0' to 'categories/9'
    3.1.2. With this in mind, I built the script assuming that I will have to run through ten columns specifically and concatenate the data into the added "Categories" column, with a comma separator
    3.1.3. Also, in the "Prep Parameters" sheet, which basically is the script's guide for filtering out the unwanted columns, renaming the remaining columns, and grouping and sorting the columns from left to right, I specifically included 10 columns for categories
    3.1.4. So color me shocked and frustrated when I realized that some of the APIFY resulting CSVs don't have 10 columns exactly, but sometimes less, and (this is just an assumption), potentially could be even more
    3.1.5. Point is, I built the script assuming this column count is constantly 10, but apparently it's variable
  3.2. The solution:
    3.2.1. The solution I'm envisioning is rather simple really
    3.2.2. The "Prep Parameters" sheet's classification of the columns must be disregarded, as this is a really special case when it comes to the processing of the columns
      3.2.2.1. What I mean is, the other columns simply go through a simple process of being filtered out, then renamed, then grouped and sorted, while the categories columns and the opening hours columns go through filtering out, adding a new column with data formulated from other columns, then renamed, then grouped and sorted, so this additional step is what makes them exceptions
    3.2.3. What's hard about this is that I have to now think of these exception cases as separate feature relative to the simpler ones, which I do believe is a good thing as that makes the debugging easier if we compartmentalize them, it's just a hassle to do really
    3.2.4. Once compartmentalization is done, I just need to then change the script for getting all the categories columns, in that instead of fetching a specific number of columns, it will look for all columns that match the format
    3.2.5. This way, there's no need to be changing the Prep Parameters at all, as that will simply just be a guide for the non-exception columns
    3.2.6. Also this way, I can just go ahead and plop any number of sheets within the "input" folder and run the script, producing their corresponding output files into the "output" folder
    3.2.7. Another great idea is to enable the script to compile ALL output CSVs into one excel/gsheets file
    3.2.8. Also, definitely need to fix the group headers, as it's a freaking hassle to do manually