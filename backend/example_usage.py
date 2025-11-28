"""
Example usage of the Multi-Agent System
Run this file to see how the agents work
"""
from agents.orchestrator import MultiAgentOrchestrator

def main():
    """
    Demonstrate the multi-agent system
    """
    print("=" * 60)
    print("MULTI-AGENT AI SYSTEM DEMO")
    print("=" * 60)
    
    # Initialize orchestrator
    orchestrator = MultiAgentOrchestrator()
    
    # Get agents info
    print("\n📋 Available Agents:")
    info = orchestrator.get_agents_info()
    for agent in info['agents']:
        print(f"  - {agent['name']}: {agent['description']}")
    
    # Example 1: Test Content Moderator
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Content Moderation")
    print("=" * 60)
    test_text_1 = "Hello team, great work on the project!"
    print(f"\n📝 Input: {test_text_1}")
    print("\n🔍 Running Content Moderator Agent...")
    
    result_1 = orchestrator.process_single_agent(test_text_1, "moderator")
    print(f"\n✅ Result:")
    print(f"   Analysis: {result_1.get('analysis', 'N/A')}")
    
    # Example 2: Test Cat Translator
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Cat Translation")
    print("=" * 60)
    test_text_2 = "I'm so excited for the weekend!"
    print(f"\n📝 Input: {test_text_2}")
    print("\n🐱 Running Cat Translator Agent...")
    
    result_2 = orchestrator.process_single_agent(test_text_2, "translator")
    print(f"\n✅ Result:")
    print(f"   Cat Translation: {result_2.get('cat_translation', 'N/A')}")
    
    # Example 3: Full Pipeline
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Full Pipeline (Both Agents)")
    print("=" * 60)
    test_text_3 = "Thank you for your help!"
    print(f"\n📝 Input: {test_text_3}")
    print("\n🔄 Running Full Pipeline...")
    print("   Step 1: Content Moderation")
    print("   Step 2: Cat Translation")
    
    result_3 = orchestrator.process_pipeline(test_text_3)
    print(f"\n✅ Final Output:")
    print(f"   {result_3.get('final_output', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("NOTE: Replace API key in simple_agent.py for real OpenAI calls")
    print("=" * 60)

if __name__ == "__main__":
    main()
