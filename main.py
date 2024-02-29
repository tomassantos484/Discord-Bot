@client.tree.command(name="troutify", description="Mike Trout sends a random statement about himself!")
async def troutify(interaction: discord.Interaction):
    def getResponse(model, query):
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
            },
            data=json.dumps({
                "model": model,
                "messages": [{"role": "user", "content": query}],
            })
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API call failed with status code {response.status_code}")
            return None

    # Call the function and store the response
    response = getResponse("gryphe/mythomist-7b:free", "Generate a random funny/semi-satirical baseball-related statement about Mike Trout.")

    if response and 'choices' in response and len(response['choices']) > 0:
        # Access and send the statement
        statement = response['choices'][0]['message']['content']
        await interaction.response.send_message(statement, ephemeral=False)
    else:
        # Handle error or empty response
        error_message = "Sorry, I couldn't fetch a statement for Mike Trout at the moment."
        await interaction.response.send_message(error_message, ephemeral=False)
