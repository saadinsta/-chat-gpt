import openai
import streamlit as st

# استخدم الرمز المخفي الخاص بك للوصول إلى Assistants API
openai.api_key = "YOUR_API_KEY_HERE"

# انشاء نموذج ذاتي يتعامل مع ملفات ويعتمد عليها في الرد مع ChatGPT
assistant = openai.Assistant(
    name="My Chat Assistant",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# انشاء نقطة تحديد للمحادثة بين المستخدم والبوت
thread = openai.Thread.create()

# اضافة رسالة جديدة إلى النقطة بواسطة المستخدم والتحقيق من أي ملفات يجب عليها نموذج البوت للتعامل معها
message = openai.Thread.Message.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# تشغيل نموذج البوت للتحقيق من الردود على الرسائل المضافة إلى النقطة
run = openai.Thread.Run.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)

# تحقيق من الحالة المتقدمة للتشغيل للبوت للتحقيق من أي ملفات يجب عليها نموذج البوت للتعامل معها
run = openai.Thread.Run.retrieve(
    thread_id=thread.id,
    run_id=run.id
)

# عرض الردود المحاولة لنموذج البوت على المستخدم بواسطة الرسائل المضافة إلى النقطة
messages = openai.Thread.Message.list(
    thread_id=thread.id
)

# والتحقيق من أي ملفات يجب عليها نموذج البوت للتعامل معها
run.steps

# عرض الرسائل على واجهة Streamlit
st.write("User message:", message.content)
st.write("Assistant response:", run.steps[-1].content)
