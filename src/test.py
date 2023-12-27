import pandas as pd

data={
  "speaker_0": [
    "Hi Emmett, it's good to meet you today. Before we begin, I want you to know that our conversation is confidential, and I'm here to help and support you.",
    "I understand that you were referred to me by your GP. They mentioned that you've been feeling quite down recently. Could you tell me a bit more about what you've been experiencing?",
    "From your notes, I saw that you visited the GP about three months ago. How long have you been feeling down altogether?",
    "Has it gotten worse since you saw your GP?",
    "Tell me, Emmett, how are things at the moment?",
    "You mentioned feeling really down and lacking motivation. Are you okay?",
    "You've been quite isolated, and there aren't many people around.",
    "You're an English student at uni, living away from home with some friends, right?",
    "You feel like you live with your friends, but you don't feel like you can talk to them. Do you try to hide the way you're feeling from them?",
    "It sounds like you've been feeling down and unmotivated. You want to be better, but it seems challenging to reach out for help.",
    "When did all of this start? Around last March or April?",
    "A lot was happening, with uni pressure and your parents' marital problems. That must have been a real shock for you.",
    "You tried to work hard and be more successful, thinking it would make things better. How did it backfire?",
    "After the summer and exams, how did that period go for you?",
    "It sounds like you had an awful lot going on, and it would be understandable not to do as well as normal. Do you have very high standards for yourself?",
    "It was a difficult time for you, and your mood has remained low. What's the situation with your parents now?",
    "Were you home over the summer?",
    "How was that?",
    "A lot has been happening. You've been feeling very low, with uni pressure and problems in your parents' marriage. You feel like you can't reach out to anyone. Can you tell me more about how you've been feeling this past week?",
    "Let's think about one thing, like a lecture. What kind of thoughts do you have before it happens?",
    "It sounds like you think it's pointless and not worth it. Any other thoughts before you go to the lecture?",
    "It seems like you feel you're not as good as other people here. Is that accurate?",
    "Is it okay if I take notes as we go through? It helps me understand, and I'll share this with you later.",
    "Those are quite negative thoughts. How do you feel when you have them?",
    "You described thoughts of being unworthy and should be doing things better. What kind of emotions do you feel?",
    "I notice you're laughing as we talk about these emotions. How do you feel about discussing them?",
    "You're doing a great job. Some thoughts are pointless, not worth it, and you're unworthy. What about the emotions and physical feelings associated with them?",
    "It's draining you of energy, and you're noticing sleep problems. What do you do when these thoughts occur?",
    "You dwell on those worries and stay in bed. Have you tried talking to friends or family about it?",
    "How do you feel after staying in bed and focusing on those thoughts? Better or worse?"
  ],
  "speaker_1": [
    "Yeah, I've been feeling quite bad for quite a while now, and I thought maybe it's time to see someone about it because I don't want to feel like this anymore.",
    "It started feeling a bit low a few months ago, but it's gotten pretty bad recently.",
    "I've been feeling bad for quite a while, so I thought it's time to seek help.",
    "I've been feeling a bit low and wound up about things, but recently, I can't be bothered to do anything at all. I find it hard to get motivated. I want to be better, but it's reaching the point where I need to do something about it.",
    "It's hard because there's not really anyone to talk to. I just stay on my own and try not to think about it.",
    "No one I can talk to about it understands anyway.",
    "I get on well with my friends, but I don't want to bring them down. They don't understand what I'm going through.",
    "It's easier to hide it than to try and explain it. I don't really talk to my parents about it either.",
    "It started when I was revising for exams, putting a lot of stress on myself. My parents were going through a troubled time then.",
    "I felt guilty, thinking if I could do better, things would get better. But it backfired, and I've been feeling worse since then.",
    "I know I should have done better, and I beat myself up a lot about it. I have high standards for myself.",
    "I don't talk to my parents a lot, but it doesn't sound good. I don't like to talk to them about it because it makes me feel worse.",
    "I was home over the summer, but it wasn't very fun. It stressed me out more than relaxed me.",
    "I focus on negative thoughts, stay in bed, and dwell on worries. I haven't tried talking to friends or family about it.",
    "I feel slightly worse, a bit numb. It's almost nicer not to think about it at all.",
    "It's draining, and physically, I feel tense. There's a heaviness in my chest.",
    "When those thoughts come, I usually isolate myself and stay in bed. It's like a cycle.",
    "I haven't really talked to anyone about it. It's hard to explain what I'm going through.",
    "After staying in bed and dwelling on those thoughts, I feel worse. It's like a heavy burden on my shoulders.",
    "It feels like a relief, but at the same time, I know it might make things worse in the long run.",
    "It feels like I don't deserve to be here, and I question my purpose at uni. I see others doing well, and I feel out of place.",
    "I feel unworthy and lower than normal. It makes me think about all the things I should have been doing better.",
    "Talking about these emotions is uncomfortable for me. I've never really had to discuss them before.",
    "Physically, it's draining. I feel lethargic, and my body can't be bothered to do anything. Sleep is elusive, and it adds to the frustration.",
    "I try to distract myself, but those thoughts linger. It's like a cloud hanging over me.",
    "I haven't really reached out to anyone. It's hard for me to open up about what I'm going through.",
    "After dwelling on those thoughts, I feel worse. It's like I've exhausted myself emotionally and physically.",
    "It's a mix of emotions. Part of me feels relieved, but there's also a sense of numbness. It's a complex emotional state.",
    "In the long run, I know avoiding things might not be the solution, but in the moment, it provides a temporary escape.",
    "It's challenging to see a way out of this cycle. The negative thoughts keep reinforcing themselves.",
    "I'm not sure how to break this cycle. It feels like a constant struggle, and I don't see a clear path forward."
  ]
}



# Find the maximum length of the arrays in speaker_0 and speaker_1
max_len = max(len(data["speaker_0"]), len(data["speaker_1"]))

# Pad the shorter array with "-" to make them equal in length
data["speaker_0"] += ["-"] * (max_len - len(data["speaker_0"]))
data["speaker_1"] += ["-"] * (max_len - len(data["speaker_1"]))

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Remove rows where speaker_1 is empty or contains the word "you"
df = df[df["speaker_1"].str.strip() != ""]
df = df[~df["speaker_1"].str.contains("you")]

# Reset index
df = df.reset_index(drop=True)

# Save the cleaned DataFrame to a CSV file
df.to_csv('cleaned_conversation.csv', index=False)