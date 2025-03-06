# forecast_ai

I started the project with the gpt-4o-mini model and have since switched to the o3-mini model in OpenAI's Assistants API:
The responses.txt file features old responses from the 4o-mini model, but new responses are written to the responses_o3.txt file.

documentation for how the Asistants APi works can be found here: https://platform.openai.com/docs/assistants/overview

The python file currently requires the user to manually change the date variable. This means the user can also set the date to the past to have the prompt tell the AI to behave as if it is this date in the past. There is not enough data yet to confirm with certainty that the responses for retroactively querying the assistant are the same as querying the assistant on the current date (ie. asking it to answer as if it is March 1, on March 5 yields the same result as asking it on March 5).
