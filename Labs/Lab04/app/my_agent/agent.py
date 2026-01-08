import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

# THE TOOL: This skill allows the bot to fetch real stats
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import time


def get_player_season_stats(player_name: str) -> str:
    """Retrieves the most recent season statistics for an NBA player."""
    try:
        import time
        from nba_api.stats.endpoints import playercareerstats
        from nba_api.stats.static import players

        time.sleep(1.0) # Rate limit protection

        search_results = players.find_players_by_full_name(player_name)
        if not search_results:
            return f"No player found named {player_name}"

        player_id = search_results[0]['id']
        career = playercareerstats.PlayerCareerStats(player_id=player_id)

        # FIX: Access the raw data dictionary instead of using a pandas DataFrame
        # This removes the dependency on pandas entirely
        data_dict = career.get_dict()
        latest_row = data_dict['resultSets'][0]['rowSet'][-1]
        headers = data_dict['resultSets'][0]['headers']

        # Mapping common stats by their position in the raw NBA API list
        stats = dict(zip(headers, latest_row))

        return (f"{player_name} ({stats['SEASON_ID']}): {stats['PTS']} PPG, "
                f"{stats['AST']} APG, {stats['REB']} RPG")

    except Exception as e:
        return f"NBA API Error: {str(e)}"
        
# THE BRAIN: Standard connection to Groq/OpenAI
client = OpenAIChatClient(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY") ,
    model_id=os.getenv("MODEL")
)

# THE BOT: Persona and Tool assignment
nba_bot = ChatAgent(
    chat_client = client,
    name="NBA Analyst",
    instructions="""
        You are a knowledgeable NBA analyst.
        When asked about a player's performance, you MUST use the
        'get_player_season_stats' tool to provide factual data.
    """,
    tools=[get_player_season_stats],
    additional_chat_options={
            "timeout": 60.0
    }
)

# THE ON-SWITCH: Export for Dev UI
agent = nba_bot