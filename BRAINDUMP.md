Scraper almost perfect, fixes needed

1. Did the scraper, reviewed a bit but not too much cuz I'm on a bit of a time crunch (will have to review later when I have the time), and after bit of tweaking for the inputs and outputs and after debugging with ChatGPT for 2 errors, I managed to produce an output that's quite close to the expected
  1.1. One error is that the original script was producing the Opening Hours compiled by getting the data from openingHours/0/hours etc, when these columns have already been renamed, so I just renamed the column fetch to the renamed versions, Monday etc
  1.2. The second error is a bit more vague, and GPT-san explained it as ff:
    1.2.1. The error message you're encountering indicates that there is a nan value in the final_columns list, which is causing the KeyError when trying to reorder the DataFrame. To resolve this, we need to ensure that there are no nan values in the column names list and that all column names exist in the DataFrame. 
    1.2.2. The solution is:
      1.2.2.1. Removing nan Values: Added a step to remove any potential nan values from the final_columns list.
      1.2.2.2. Existing Columns Check: Before reordering, it checks if all columns in final_columns exist in the DataFrame and filters out the missing ones, issuing a warning if any are missing.
2. Some issues that I found that still need fixing are:
  2.1. There are actually 2 rows of headers, not just one, and row 1 should be the column group titles, and row 2 the actual column names
  2.2. The hours, for some reason, are being rendered into the output as "7â€¯AM to 5â€¯PM", for example, when I know for a fact that the input is simply "7 AM to 5 PM"