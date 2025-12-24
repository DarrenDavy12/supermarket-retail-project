# Simulate ADF Orchestration

# Step 1: Bronze -> Silver
dbutils.notebook.run("bronze_silver", 60) # runtime 60 seconds/minute 

# Step 2: Silver -> Gold
dbutils.notebook.run("gold", 60) # runtime 60 seconds/minute
