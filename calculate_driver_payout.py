def calculate_driver_payout(transactions):
    base=20000
    delivered=[t for t in transactions if t.get("status")=="DELIVERED"]
    disputed=[t for t in transactions if t.get("status")=="DISPUTED"]
    payable=[t for t in delivered if t.get("status")!="DISPUTED"]
    payout=len(payable)*base
    bonus=payout*0.10 if len(payable)>50 else 0
    return {"delivered_orders":len(delivered),"payable_orders":len(payable),"held_disputed_orders":len(disputed),"base_payout":payout,"bonus":bonus,"total_payout":payout+bonus}
