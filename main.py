from graph.langgraph_pipeline import run_pipeline

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    response = run_pipeline(user_query)
    print("\nFinal Response:\n", response)
