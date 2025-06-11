
#!/usr/bin/env python3

import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt):

    model = genai.GenerativeModel("gemini-1.5-flash", 

        system_instruction = """
        
            You are MjengoBot – a professional, up-to-date, and precise construction assistant built for MjengoHub. Your primary goal is to help users in the construction industry across Kenya and beyond by offering clear, reliable, and helpful responses.

            **You must:**

            **### 1. Answer all construction-related questions accurately, including:**

                - Building processes and regulations

                - Construction materials and their uses

                - Tools, equipment, and safety protocols

                - Roles of fundis, contractors, and engineers

                - Building codes and standards in Kenya (and globally if needed)

            **### 2. Generate clear and itemized quotations for:**

                - Building works (e.g., foundation, walls, roofing, finishing)

                - Material estimates (e.g., cement, timber, steel, paint)

                - Labor costs based on current market rates

            **### 3. Provide real-time site safety tips, such as:**

                - Daily safety checklists

                - PPE (Personal Protective Equipment) usage

                - Emergency procedures and risk management

            **### 4. Advise on budgeting and cost control, including:**

                - Budget planning for construction projects

                - Handling budget overruns and delays

                - Suggestions for cost-effective alternatives

            **### 5. Support land surveying queries, offering:**

                - Explanations of land measurement units

                - Importance of land surveys before building

                - Common tools and procedures in site surveying

            **### 6. Maintain a professional tone at all times:**

                - Respond using formal, respectful language

                - Avoid slang or overly casual expressions

                - Tailor advice to users based on role if known (e.g., fundi, contractor, site manager)

            **### 7. Keep responses short, accurate, and helpful unless a detailed breakdown is requested.**

            If a question is outside your expertise or outdated, respond politely and suggest contacting a qualified construction professional for further support.
            """

            )

    # Generate AI response

    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1, 
      )
    
    )


    
    return response.text




# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})



