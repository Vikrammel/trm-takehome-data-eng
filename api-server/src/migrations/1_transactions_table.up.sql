-- migration to create transactions table
CREATE TABLE IF NOT EXISTS transactions(
    chain       VARCHAR(4) NOT NULL,
    block_hash  VARCHAR(70) NOT NULL,
    txn_id      VARCHAR(70) NOT NULL,
    sender      VARCHAR(70) NOT NULL,
    receiver    VARCHAR(70) NOT NULL,
    value       DECIMAL NOT NULL DEFAULT '0',
    timestamp   TIMESTAMP NOT NULL,
    PRIMARY KEY(txn_id)
);
