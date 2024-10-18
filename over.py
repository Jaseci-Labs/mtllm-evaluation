# import re

# def generate_response(query: str, chat_history: dict[str,str], user_data:dict) -> tuple[str,int]:
#     retrived_info_with_rag = rag_engine.retriver(query = query)
#     system_message = (
#         "You are a chatbot. Respond to the chat using the available information.\n" )
    
#     prompt =  system_message
#     prompt += f'\nQuery\n{query}'
#     prompt += f'\nChat History:\n'
#     for user,content in chat_history:
#         prompt += f'{user} : {content} \n'
#     prompt += f'\nChat History:\n'
#     for key,value in user_data:
#         prompt += f'{key} : {value} \n'
#     prompt += f'\nRetrived Information:\n'
#     for chunks in retrived_info_with_rag:
#         prompt += f'{chunks} \n'
#     prompt += f'\nChat Response: <output>'
#     prompt += f'\n(How Relevent was the rag information out of 5)\n'
#     prompt += f'Rating: <output>'

#     response = llm.infer(prompt)

#     lines = response.strip().split('\n')
#     for line in lines:
#     if line.startswith("Chatbot Response:"):
#         chatbot_response = line[len("Chatbot Response:"):].strip()adjest aeron
#         sddfsdfsdfsdfsdf

#     return chatbot_response, rating_value

def generate_response(query: str, 
        chat_history: dict[str,str], 
        user_profile_data:dict,
        retrived_info:list) -> tuple[str,int]:
    
    system_message = (
        "You are a chatbot. Respond to the chat using the available information.\n" )
    
    prompt =  system_message
    prompt += f'\nQuery\n{query}'
    prompt += f'\nChat History:\n'
    for user,content in chat_history:
        prompt += f'{user} : {content} \n'
    prompt += f'\nChat History:\n'
    
    for key,value in user_profile_data:
        prompt += f'{key} : {value} \n'
    prompt += f'\nRetrived Relevent Information using a RAG system:\n'
    
    for chunks in retrived_info_with_rag:
        prompt += f'{chunks} \n'
    prompt += f'\nChatbot Response: <output>'

    response = llm.infer(prompt)

    lines = response.strip().split('\n')
    for line in lines:
        if line.startswith("Chatbot Response:"):
            chatbot_response = line[len("Chatbot Response:"):].strip()

    return chatbot_response

output = generate_response(query,
                        chat_history,
                        user_data,
                        rag_engine.retriver(query = query))


def respond_with_confidence_level(query: str, 
    chat_history: dict[str,str], 
    user_data:dict,
    retrived_info:list) -> tuple[str,float]:

    system_message = (
        "You are a chatbot. Respond to the chat using the available information.\n Additionally generate a confidance level of the response as a percentage" )
    
    prompt =  system_message
    prompt += f'\nQuery form the user:\n{query}'
    prompt += f'\nChat History:\n'
    for user,content in chat_history:
        prompt += f'{user} : {content} \n'
    prompt += f'\nUser Information:\n'
    for key,value in user_data:
        prompt += f'{key} : {value} \n'
    prompt += f'\nFollow the format given below for response.'
    prompt += f'\nEnd response with newline.'
    prompt += f'\nGive confidence level as a float.'
    prompt += f'\nResponse:<output>\n'
    prompt += f'\nConfidence:<output>\n'
    
    response = llm.infer(prompt)
    
    lines = response.strip().split('\n')
    for line in lines:
        if line.startswith("Response:"):
            chatbot_response = line[len("Response:"):].strip()
        elif line.startswith("Confidence:"):
            confidence_level = line[len("Confidence:"):].strip()
            try:
                confidence_level = float(confidence_level)
            except:
                confidence_level = 50.0
        
    return (chatbot_response, confidence_level)