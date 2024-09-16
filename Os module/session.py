from sqlalchemy import Column, String, ForeignKey, create_engine, Integer, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

from test import engine, SubscribedPlan, SubscriptionPlan, SubscriptionMethod

Session = sessionmaker(bind=engine)

session = Session()

def ValidateSubs(U_id, Subs_Id):
    user = session.query(SubscribedPlan).filter_by(user_id == U_id)
    if not user:
        return f"user does not exist"
    subsID = session.query()
        
    return 