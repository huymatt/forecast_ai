
from openai import OpenAI
import os
import time

# Set the working directory
os.chdir("/Users/matthuy/desktop/python/Edith")
 
OPENAI_API_KEY = "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"

client = OpenAI(api_key=OPENAI_API_KEY)

assistant_id = "asst_6oyti5zbfh27NnwYTrrmKubw"
thread_id = "thread_nauRns2Cb6sCJnaij6SgJlvF"

# Step 1: Load or Create Assistant
#if os.path.exists(assistant_id):
#    with open(assistant_id, "r") as f:
#        assistant_id = f.read().strip()
#else:
#    my_assistant = client.beta.assistants.create(
#        model="o3-mini",
#        name="forecaster_o3",
#        instructions="You are a participant on a panel of professional economic forecasters.",
#    )
#    assistant_id = my_assistant.id
#    with open(assistant_id, "w") as f:
#        f.write(assistant_id)

# Step 2: Load or Create Thread
#if os.path.exists(thread_id):
#    with open(thread_id, "r") as f:
#        thread_id = f.read().strip()
#else:
#    my_thread = client.beta.threads.create()
#    thread_id = my_thread.id
#   with open(thread_id, "w") as f:
#       f.write(thread_id)



# Define forecasting parameters
date = "March 5, 2025"
variables = "Real GDP, CPI inflation, Core CPI inflation, Headline PCE inflation, Core PCE inflation, Industrial Production, unemployment, initial jobless claims, federal funds rate, 10-year yield"
release_date = "February 19, 2025"

# Step 3: Format the Message Properly
question = (
    f"We are in {date}. You are about to fill out the forecast form for {date}. "
    f"Using only the information available to you as of {date}, please provide your best numeric forecast "
    f"for the following variables: {variables}. Do this for the following quarters: t (current quarter), t+1, t+2, t+3, "
    f"and t+4, as well as annual forecasts for this and next year (annual averages). "
    f"You have the most recent real-time data on key macroeconomic variables available to you as of today: {date}. "
    f"Do not incorporate any data that was not available to you beyond the current date in your forecasts. "
    f"Do consider all relevant information on the broad economic conditions and current Federal Reserve actions "
    f"(up to, but not beyond {release_date}). Use available information, and your professional judgment and experience. "
    f"Your forecast is anonymous. Provide the forecasts as a sequence of numerical values only. "
    f"Please only provide your forecasts in the format: (t, t+1, t+2, t+3, t+4, this year’s average, next year’s average)."
)

# Send the message
my_thread_message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=question,
)
print(f"This is the message object: {my_thread_message} \n")

# Step 4: Run the Assistant
my_run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
)
print(f"This is the run object: {my_run} \n")

# Step 5: Poll the Run Status
while True:
    my_run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=my_run.id
    )
    
    if my_run.status == "completed":
        break
    elif my_run.status not in ["queued", "in_progress"]:
        print(f"Run failed with status: {my_run.status}")
        break  # Exit the loop if there's an error
    time.sleep(2)  # Wait before checking again

# Step 6: Retrieve the Assistant's Response
all_messages = client.beta.threads.messages.list(
    thread_id=thread_id
)

assistant_response = all_messages.data[0].content[0].text.value

# Step 7: Store Response in a File
with open("responses_o3.txt", "a") as file:
    file.write(f"Date: {time.strftime('%Y-%m-%d')}\n")
    file.write(f"User: {question}\n")
    file.write(f"Assistant: {assistant_response}\n\n")

print("Response saved successfully!")
