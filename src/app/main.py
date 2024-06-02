@app.get("/history")
def get_history(type: str, value: int, current_balance: float, timestamp: float):

    return{
  "all_transactions": [
    {
      "type": "deposit",
      "value": 100.0,
      "current_balance": "1000.0",
      "timestamp": 1690482853890
    },
    {
      "type": "withdraw",
      "timestamp": 1691707985704.6152,
      "current_balance": 700.0,
      "value": 300
    }
  ]
}