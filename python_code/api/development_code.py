from agents import (GuardAgent,
                    ClassificationAgent,
                    DetailsAgent,
                    RecommendationAgent,
                    AgentProtocol,
                    )
import os

def main():
    guard_agent = GuardAgent()
    classification_agent = ClassificationAgent()

    recommendation_agent = RecommendationAgent(
        '/Users/aungnandaoo/Desktop/AI_Integrated_Coffee_Shop_App/python_code/api/recommendation_objects/apriori_recommendations.json',
        '/Users/aungnandaoo/Desktop/AI_Integrated_Coffee_Shop_App/python_code/api/recommendation_objects/popularity_recommendation.csv'
    )

    agent_dict: dict[str, AgentProtocol] = {
        "details_agent": DetailsAgent(),
        "recommendation_agent" : recommendation_agent
    }

    messages = []
    while True:
        # Display the chat history
        # os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\nPrint Messages ...............")
        for message in messages:
            print(f"{message['role'].capitalize()}: {message['content']}")

        # Get user input
        prompt = input("User: ")
        messages.append({"role": "user", "content": prompt})

        # Get GuardAgent's response
        guard_agent_response = guard_agent.get_response(messages)

        if guard_agent_response["memory"]["guard_decision"] == "not allowed":
            messages.append(guard_agent_response)
            continue
        # Get ClassificationAgent's response
        classification_agent_response = classification_agent.get_response(messages)
        chosen_agent=classification_agent_response["memory"]["classification_decision"]
        print("Chosen Agent: ", chosen_agent)

        # Get the chosen agent's response
        agent = agent_dict[chosen_agent]
        response = agent.get_response(messages)
        
        messages.append(response)

# Add this to execute main
if __name__ == "__main__":
    main()
