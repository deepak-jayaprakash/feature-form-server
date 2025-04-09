-- Create transactions table
CREATE TABLE transactions (
    transactionid VARCHAR(10) PRIMARY KEY,
    customerid VARCHAR(10) NOT NULL,
    customerdob DATE NOT NULL,
    custlocation VARCHAR(50) NOT NULL,
    custaccountbalance DECIMAL(10,2) NOT NULL,
    transactionamount DECIMAL(10,2) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    isfraud BOOLEAN NOT NULL
);

-- Insert sample data
INSERT INTO transactions VALUES
('T1', 'C5841053', '1994-10-01', 'JAMSHEDPUR', 17819.05, 25.00, '2022-04-09 11:33:09+00', false),
('T2', 'C5841053', '1994-10-01', 'JAMSHEDPUR', 17794.05, 100.00, '2022-04-09 12:15:22+00', false),
('T3', 'C5841053', '1994-10-01', 'JAMSHEDPUR', 17694.05, 150.00, '2022-04-09 13:45:10+00', true),
('T4', 'C1214240', '1985-03-15', 'MUMBAI', 25000.00, 75.50, '2022-04-09 10:20:15+00', false),
('T5', 'C1214240', '1985-03-15', 'MUMBAI', 24924.50, 200.00, '2022-04-09 11:05:30+00', false),
('T6', 'C1214240', '1985-03-15', 'MUMBAI', 24724.50, 300.00, '2022-04-09 14:30:45+00', true); 