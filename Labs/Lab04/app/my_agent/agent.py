import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# THE TOOL: This skill allows the bot to fetch real stats
def get_player_season_stats(player_name: str) -> str:
    """
    Retrieves the most recent season statistics for an NBA player.
    :param player_name: Full name of the player (e.g., 'LeBron James').
    """
    # 1. Convert name to ID
    search_results = players.find_players_by_full_name(player_name)
    if not search_results:
        return f"Could not find statistics for '{player_name}'."
    
    player_id = search_results[0]['id']
    
    # 2. Fetch career stats
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    stats_df = career.get_data_frames()[0]
    
    # 3. Format the latest season data
    latest_season = stats_df.iloc[-1]
    return (f"{player_name} ({latest_season['SEASON_ID']}): "
            f"Team: {latest_season['TEAM_ABBREVIATION']}, "
            f"Games: {latest_season['GP']}, Points: {latest_season['PTS']}, "
            f"Assists: {latest_season['AST']}, Rebounds: {latest_season['REB']}.")

# THE BRAIN: Standard connection to Groq/OpenAI
client = OpenAIChatClient(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY"),
    model_id=os.getenv("MODEL")
)

# THE BOT: Persona and Tool assignment
nba_bot = ChatAgent(
    chat_client=client,
    name="NBA Analyst",
    instructions="""
        You are a knowledgeable NBA analyst. 
        When asked about a player's performance, you MUST use the 
        'get_player_season_stats' tool to provide factual data.
    """,
    tools=[get_player_season_stats]
)

# THE ON-SWITCH: Export for Dev UI
agent = nba_bot