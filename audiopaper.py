def generate_report(score, answers):
    report = "\n🔍 Personalized Audio Perception Report\n"
    report += "-----------------------------------------\n"

    # Adaptability and Attention Summary based on answers
    if answers[0] == "A":
        report += "Q1: You perceived the rain sound as peaceful. This suggests high adaptability to calming sounds. You likely find it easy to adjust to tranquil environments.\n"
    elif answers[0] == "B":
        report += "Q1: You perceived the rain sound as confusing. You might struggle with sounds that lack clear structure, which could suggest lower adaptability to chaotic or ambient noise.\n"
    else:
        report += "Q1: You didn't find the rain sound particularly special. This may indicate a neutral response to ambient sounds, with potential difficulty in engaging deeply with them.\n"

    if answers[1] == "A":
        report += "Q2: You felt calm while listening to the rain. Your ability to focus in peaceful environments is strong, suggesting a good attention span in low-distraction settings.\n"
    elif answers[1] == "B":
        report += "Q2: You felt tense while listening to the rain. You may need extra support in environments with ambient sounds, as they can trigger feelings of unease.\n"
    else:
        report += "Q2: You felt neutral while listening to the rain. This could mean you are adaptable but may need specific sounds to engage deeply.\n"

    if answers[2] == "A":
        report += "Q3: You imagined a forest or garden while listening to birds. This indicates that you may have a strong connection to nature or calming sounds, possibly reflecting a preference for peaceful environments.\n"
    elif answers[2] == "B":
        report += "Q3: You imagined a noisy place while hearing the birds. You might thrive in dynamic environments, which could indicate a preference for more stimulating or energetic auditory cues.\n"
    else:
        report += "Q3: You didn’t imagine anything while listening to the birds. This suggests that you may need more context or a more defined auditory environment to process and engage with sounds.\n"

    if answers[3] == "A":
        report += "Q4: You felt that the bird sounds helped you concentrate. This is a strong indication of your ability to filter out distractions and focus on relevant stimuli.\n"
    elif answers[3] == "B":
        report += "Q4: You felt distracted by the bird sounds. You may need quieter or more controlled environments to stay focused.\n"
    else:
        report += "Q4: You are unsure whether the bird sounds helped you concentrate. This may suggest variability in how you respond to sound-based stimuli.\n"

    # Halloween audio question (handling multi-answer)
    matched_words = ", ".join(answers[4]) if len(answers[4]) > 0 else "none"
    report += f"\nQ5: You recognized the words: {matched_words}. This indicates your ability to recall specific auditory details. The recognition of many words suggests good auditory processing and memory.\n"

    # Final score and learning type classification
    report += "\n🎯 Final Audio Score: {:.2f} / 6".format(score)

    if score >= 5:
        report += "\n🧠 Result: Strong Audio Learner 🎧\nYou have an excellent ability to perceive, process, and engage with audio cues. You can focus in calming environments and may benefit from sound-based learning tools. Future Focus: Keep refining auditory learning techniques for focus and memory retention."
    elif score >= 3:
        report += "\n🧠 Result: Moderate Audio Learning Ability\nYou can process and engage with sounds, but you may require a balanced environment. Your learning style could benefit from a mix of audio and other sensory inputs. Future Focus: Explore techniques that combine sound with visual or kinesthetic stimuli to enhance engagement."
    else:
        report += "\n🧠 Result: Limited Audio Learning Ability\nYou may find it difficult to engage with audio-based learning, and sounds might be distracting or neutral for you. Future Focus: Consider exploring more visual or kinesthetic learning methods, such as video tutorials or hands-on activities. You may thrive in quieter, more controlled environments."

    # Neurodivergent Considerations (based on responses)
    report += "\n\n🧠 Neurodivergent Considerations:"
    
    if score < 3:
        report += "\n- It’s possible that you may have difficulty with processing auditory stimuli, which is common in neurodivergent individuals who prefer visual or kinesthetic methods of learning. Sound may be overwhelming or distracting, and alternative approaches like visual aids or interactive activities might suit you better."
    else:
        report += "\n- Your ability to engage with sounds may indicate that you are adaptable in certain environments. However, variations in attention span or adaptability might suggest that you benefit from a tailored learning environment that provides a mix of auditory and other sensory stimuli."

    return report


def audio_learning_test():
    print("\n🔊 AUDIO PERCEPTION TEST")
    print("You will listen to 3 audio files outside this program.")
    print("After each one, answer the questions below honestly.\n")
    
    score = 0
    answers = []

    print("🎵 1. Listen to 'rain_sound.mp3'")
    input("Press Enter when done listening...")

    print("\nQ1. What does this sound remind you of?")
    print("A. Peace\nB. Confusion\nC. Nothing special")
    ans1 = input("Your answer: ").strip().upper()
    answers.append(ans1)
    if ans1 == "A":
        score += 1

    print("\nQ2. Did you feel calm or tense while listening?")
    print("A. Calm\nB. Tense\nC. Neutral")
    ans2 = input("Your answer: ").strip().upper()
    answers.append(ans2)
    if ans2 == "A":
        score += 1

    print("\n🎵 2. Listen to 'bird_chirp.mp3'")
    input("Press Enter when done listening...")

    print("\nQ3. What did you imagine while hearing it?")
    print("A. A forest or garden\nB. A noisy place\nC. Nothing")
    ans3 = input("Your answer: ").strip().upper()
    answers.append(ans3)
    if ans3 == "A":
        score += 1

    print("\nQ4. Did this sound help you concentrate?")
    print("A. Yes\nB. No\nC. I don't know")
    ans4 = input("Your answer: ").strip().upper()
    answers.append(ans4)
    if ans4 == "A":
        score += 1

    print("\n🎵 3. Listen to 'halloween.mp3'")
    input("Press Enter when done listening...")

    print("\nQ5. What words did you hear? (Type all you remember)")
    expected = {"spider", "candy", "trick-or-treat", "black cat", "witch", 
                "vampire", "jack o' lantern", "skeleton", "ghost", "haunted house"}

    ans5 = input("Your words (comma-separated): ").lower().replace("’", "'").split(",")
    answers.append(ans5)
    matched = set(map(str.strip, ans5)).intersection(expected)
    score += len(matched) / len(expected) * 2  # Scaled score (out of 2)

    print("\n🎯 Final Audio Score:", round(score, 2), "/ 6")

    # Generate and display personalized report
    report = generate_report(score, answers)
    print(report)

# Run the test
audio_learning_test()


