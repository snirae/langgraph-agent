from graph.langgraph_pipeline import run_pipeline

if __name__ == "__main__":
    while True:
        user_query = input("Enter your query: ")
        response = run_pipeline(user_query)
        print("\nFinal Answer:\n", response["answers"][0])
