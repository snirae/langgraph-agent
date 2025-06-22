from graph.enhanced_rag_pipeline import EnhancedRAGPipeline


if __name__ == "__main__":
    # pipeline = SimpleRAGPipeline()
    pipeline = EnhancedRAGPipeline()
    user_query = input("Enter your query: ")
    while user_query != "":
        response = pipeline.run_pipeline(user_query)
        print(response["answer"], end=f"\n\n{'#' * 100}\n\n")

        user_query = input("Enter your query: ")
