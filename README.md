# forecast_ai

I started the project with the gpt-4o-mini model and have since switched to the o3-mini model in OpenAI's Assistants API.

The responses_4o.txt file features old responses from the 4o-mini model, but new responses are written to the responses_o3.txt file.

Documentation for how the Asistants APi works can be found here: https://platform.openai.com/docs/assistants/overview

The python file currently requires the user to manually change the date variable. This means the user can also set the date to the past to have the prompt tell the AI to behave as if it is this date in the past. There is not enough data yet to confirm with certainty that the responses for retroactively querying the assistant are the same as querying the assistant on the current date (ie. asking it to answer as if it is March 1, on March 5 yields the same result as asking it on March 5).\n

In the responses_o3.txt file:

  Date: refers to the date of running the query
  
  User: this is the prompt that was used given to the assistant, see python file and read inside the prompt to see the inputs used for {date}, {variables}, and {release_date}
  
      {date} corresponds to the date you want the AI to use for real-time data, the date you want it to         "pretend like it is."
      
      {variables} the variables you want it to forecast, these are from the bluechip survey
      
      {release_date} the date of the latest FOMC release.
      
  Assistant: this is the assistant's output, each line corresponds to one of the forecasted variables, with values for the current quarter (t), t+1, t+2, t+3, t+4, this year’s average, and next year’s average.

  
