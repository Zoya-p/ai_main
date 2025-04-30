import os

def display_image(image_path):
    # Display image to the child for them to observe
    if os.path.exists(image_path):
        print(f"\n[Displaying Image] {image_path}")
    else:
        print("\n[Image Error] Image file does not exist.")

def generate_report(score, answers):
    print("\n🎨 Generating Personalized Report based on Artistic Abilities and Perception...")

    # Report criteria
    report = "\n---- Personalized Report ----\n"
    
    # Artistic Abilities
    if score == 4:
        report += "\n✨ Artistic Potential: Exceptional\nYour ability to perceive and analyze trick questions reflects a high level of artistic creativity and critical thinking. You likely have strong spatial awareness, which is key for artistic pursuits like drawing and sculpting."
    elif score == 3:
        report += "\n✨ Artistic Potential: Advanced\nYou show strong problem-solving skills and artistic potential. You are likely very creative and able to think abstractly about shapes, volumes, and space."
    elif score == 2:
        report += "\n✨ Artistic Potential: Intermediate\nYou possess a good level of artistic awareness but may need to work on problem-solving under tricky conditions. Practice with different shapes and perspectives could help you improve."
    else:
        report += "\n✨ Artistic Potential: Beginner\nYou may find it challenging to process abstract or tricky artistic questions at first, but with consistent practice and exposure to art, you'll improve over time."

    # Cognitive Processing & Problem-Solving
    if "C" in answers[0]:  # Iron vs. Feather
        report += "\n💡 Cognitive Processing: Strong Analytical Skills\nYou displayed excellent logical thinking by understanding the trick with the weights. You can separate perception from reality, an important skill for artistic design."
    else:
        report += "\n💡 Cognitive Processing: Needs Improvement\nIt seems like you might be influenced by initial perceptions. Working on abstract thinking can help you sharpen your analysis skills."

    if "B" in answers[1]:  # Volume vs. Size
        report += "\n💡 Spatial Awareness: Excellent\nYou are good at perceiving volume and space. Your ability to understand the difference between container sizes shows great potential for artistic skills in 3D space."
    else:
        report += "\n💡 Spatial Awareness: Needs Improvement\nYou may benefit from more practice with understanding spatial relationships, such as volume and shape. Activities like building with blocks or drawing 3D objects could help."

    # Perception & Attention to Detail
    if "B" in answers[2]:  # Shadow Length
        report += "\n💡 Perception & Detail: Acute\nYou are very attentive to the subtle differences in light and shadow, a skill essential for art, especially in drawing and photography."
    else:
        report += "\n💡 Perception & Detail: Needs Practice\nYou may need to focus more on understanding how light and shadows interact. Artistic work involving light, such as painting or photography, might help improve your attention to detail."

    # Adaptability and Creativity
    if "B" in answers[3]:  # Speed and Distance
        report += "\n🎨 Adaptability and Creativity: Highly Creative\nYou can think abstractly about how things work and how different systems behave, which is excellent for creative problem-solving in the arts."
    else:
        report += "\n🎨 Adaptability and Creativity: Needs Practice\nAlthough you may struggle with abstract thinking, don't worry! With time and exposure, you will grow to think creatively about various challenges."

    # Additional factors (Optional neurodivergence considerations)
    if score <= 2:
        report += "\n⚠️ Neurodivergent Considerations: May Benefit from Additional Support\nIf you struggle with abstract concepts, you might find it helpful to receive guidance through visual aids and step-by-step instructions. This will help you build a deeper understanding of the concepts."
    else:
        report += "\n⚡ Neurodivergent Considerations: Strong Independent Problem Solver\nYour ability to solve tricky problems indicates that you are able to process information efficiently. This may mean that you excel in environments where critical thinking and hands-on learning are prioritized."

    report += "\n\n---- End of Report ----"

    print(report)

def pictorial_test():
    print("\n🖼️ Pictorial Perception Test - Trick Questions")
    print("Please answer the following tricky questions based on the images provided.\n")

    score = 0
    answers = []

    # Question 1: Iron vs Feather
    print("⚖️ 1. Which one is heavier: 1 kg of iron or 1 kg of feathers?")
    display_image("iron_vs_feather.png")  # Image of iron vs feather
    print("A. Iron\nB. Feathers\nC. Both")
    ans1 = input("Your answer: ").strip().upper()
    answers.append(ans1)
    if ans1 == "C":  # Correct answer is Both
        score += 1

    # Question 2: Volume vs. Size
    print("\n💧 2. Which container holds more water: a small, deep cup or a large, shallow bowl?")
    display_image("cup_vs_bowl.png")  # Image of a cup and a bowl with water
    print("A. Small, deep cup\nB. Large, shallow bowl\nC. Both hold the same")
    ans2 = input("Your answer: ").strip().upper()
    answers.append(ans2)
    if ans2 == "B":  # Correct answer is large, shallow bowl
        score += 1

    # Question 3: Shadow Length
    print("\n🌅 3. Which shadow is longer: the shadow at noon or the shadow at sunset?")
    display_image("tree_shadows.png")  # Image of tree shadows at different times
    print("A. Noon\nB. Sunset\nC. Both")
    ans3 = input("Your answer: ").strip().upper()
    answers.append(ans3)
    if ans3 == "B":  # Correct answer is Sunset
        score += 1

    # Question 4: Speed and Distance
    print("\n🚄 4. Which travels faster: a train or a light beam?")
    display_image("train_vs_light.png")  # Image of train and light beam
    print("A. Train\nB. Light beam\nC. Both travel at the same speed")
    ans4 = input("Your answer: ").strip().upper()
    answers.append(ans4)
    if ans4 == "B":  # Correct answer is Light beam (faster than a train)
        score += 1

    # Final report generation based on answers and score
    generate_report(score, answers)

# Running the pictorial test
pictorial_test()
