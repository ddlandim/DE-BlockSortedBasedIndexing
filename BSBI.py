import sys
import os
import numpy as np

blockFinishedCounter = 0
noBlocks = 0
textFileReaderFinished = False
normalizerFinished = False
blockReaderFinished = False

def incrementBlockFinishedCounter():
	blockFinishedCounter+=1

def getBlocksFinishedCounter():
	return blockFinishedCounter == noBlocks

def getTextFileReaderFinished():
	return textFileReaderFinished

def setTextFileReaderFinished():
	textFileReaderFinished = True

def getNormalizerFinished():
    return normalizerFinished

def setNormalizerFinished():
	normalizerFinished = True

def getBlockReaderFinished():
	return blockReaderFinished
	
def setBlockReaderFinished():
	blockReaderFinished = True

documents = os.listdir('./dataset')

noDocuments = len(documents)

documentsPerBlock = round(round(noDocuments /(np.log(noDocuments))))

blocksList = list()

blocksList = [set(documents[i:i + documentsPerBlock]) for i in range(0, len(documents), documentsPerBlock)]

termList = { -1 : "default"}
documentList = { -1 : "default"}
	
#For each block, index that block
for j in range (0,len(blocksList)):
	
	block = blocksList[j]
	
	noDocs = len(block)
	
	#normalizeQueue = new LinkedBlockingQueue<String[]>();
	#indexQueue = new LinkedBlockingQueue<String[]>();
	
	textFileReaderFinished = False
	normalizerFinished = False
	
	#TextFilesBlockReader reader = new TextFilesBlockReader(this, block, normalizeQueue)
	#BSBINormalizer normalizer = new BSBINormalizer(normalizeQueue, indexQueue, this)
	#BSBIIndexer indexer = new BSBIIndexer(indexQueue, termList, documentList, noDocs, i, this)
	
	#new Thread(reader).start();
	#new Thread(normalizer).start();
	#new Thread(indexer).start();

Print("Blocks finished. Try to merge....")

#PriorityBlockingQueue<TermPostingsList> mergeQueue = new PriorityBlockingQueue<TermPostingsList>();

# Directory and file to store indexes in...
#File invertedIndexFile = new File("index" + File.separator + "invertedindex.txt")
#File blocksDirectory = new File("blocks")

blockFinishedCounter = 0;
noBlocks = 0;

#Thread consumer;
#try {
#	consumer = new Thread(
#			new MergeIndexWriter(this, mergeQueue, invertedIndexFile)	

#for block in blocksDirectory.listFiles() :

	#Thread producer = new Thread(new BlockIndexReader(this, mergeQueue, block))
	#producer.start()
	#noBlocks++

	
	#consumer.start()