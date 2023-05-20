from fastapi import FastAPI, HTTPException

app = FastAPI()


players = {
    1786:"Cristiano ronaldo",
    666:"Messi"
}

@app.get("/player/{player_id}")
def read_player_id(player_id:int):
    if player_id not in players:
        raise HTTPException(status_code=404, detail="PlayeR ID not found")
    return {"player": players[player_id] }