from graph.enhanced_rag_pipeline import EnhancedRAGPipeline


if __name__ == "__main__":
    # pipeline = SimpleRAGPipeline()
    pipeline = EnhancedRAGPipeline(stream_response=True)
    user_query = input("Enter your query: ")
    while user_query != "":
        result = pipeline.run_pipeline(user_query)
        for token in result["answer"]:
            print(token, end="")
        print(f"\n\n{'#' * 100}\n\n")
        user_query = input("Enter your query: ")
