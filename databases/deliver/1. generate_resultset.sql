SELECT
    client,
    GROUP_CONCAT(protocol, ',') AS protocol
FROM
    traffic
GROUP BY
    client;