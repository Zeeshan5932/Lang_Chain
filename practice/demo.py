from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import OutputParser
import re

# Define a custom Output Parser class using regex
class STROutputParser(OutputParser):
    def parse(self, text: str):
        # Define the regex pattern to extract user info from the string
        pattern = r"User (\w+\s\w+) with ID (\d+) has logged in at (.+?) from IP address (\S+)"
        
        match = re.search(pattern, text)
        
        if match:
            # Return the extracted values in a structured dictionary format
            return {
                "name": match.group(1),
                "user_id": match.group(2),
                "timestamp": match.group(3),
                "ip_address": match.group(4)
            }
        else:
            raise ValueError("Could not extract data from the text.")
        
# Example raw unstructured text
raw_text = "User John Doe with ID 12345 has logged in at 2025-06-19 14:32 from IP address 192.168.1.1."

# Instantiate your custom output parser
output_parser = STROutputParser()

# Parse the raw text using the STR Output Parser
parsed_data = output_parser.parse(raw_text)

# Print the structured output
print(parsed_data)

# Output:
# {
#     'name': 'John Doe',
#     'user_id': '12345',
#     'timestamp': '2025-06-19 14:32',
#     'ip_address': '192.168.1.1'
# }
