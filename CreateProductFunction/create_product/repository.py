import logging
import random
from botocore.exceptions import ClientError
from common.exceptions import DatabaseError




logger = logging.getLogger()
logger.setLevel(logging.INFO)

pool = None


def save_product(p, n):
    conn = p.getconn()
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS ProductsTable (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), balance INT8)")
        conn.commit()
        while n > 0:
            account_balance = floor(random.random()*1_000_000)
            cur.execute("UPSERT INTO ProductsTable (id, balance) VALUES (DEFAULT, %s)", [
                        account_balance])
            logger.info(
                f"Created new ProductsTable with balance {account_balance}.")
            n -= 1
        logger.debug(f"save_product(): status message: {cur.statusmessage}")
        conn.commit()


def lambda_handler(event, context):
    

    save_product(pool, 5)

    logger.info("Database initialized.")

    return
