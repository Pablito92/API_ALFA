SELECT
	ID, TITULO,
	B.NOME AS NOME_CLIENTE,
	C.NOME AS NOME_MODULO,
	TRIM(STRFTIME('%d-%m-%Y', DATA_ABERTURA )) AS DATA_ABERTURA,
	TRIM(STRFTIME('%d-%m-%Y', DATA_ENCERRAMENTO )) AS DATA_ENCERRAMENTO
FROM TICKET A
JOIN CLIENTE B ON B.CODIGO_CLIENTE = A.CODIGO_CLIENTE
JOIN MODULO C ON C.CODIGO_MODULO = A.CODIGO_MODULO
WHERE DATA_ABERTURA LIKE '?-?-%'