spark-submit \
--queue 公司队列 \
--conf 'spark.scheduler.executorTaskBlacklistTime=30000' \
--driver-memory 10g \
--executor-memory 12g \
--conf spark.yarn.executor.memoryOverhead=3000 \
--conf spark.dynamicAllocation.maxExecutors=700 \
--conf spark.network.timeout=240s \
--conf spark.dynamicAllocation.enabled=true \
--conf spark.executor.cores=2 \
--py-files='spark_submit.zip' \ -- 注意填写自己的绝对路径
test.py --填写绝对路径
