package mrwc;

import java.io.IOException;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;

public class WordCounterJob {

	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
	if(args.length!=2){
		System.err.println("Usage:Comment wordcount <input dir><output dir>\n");
		System.exit(-1);
	}
	Job job = new Job();
	job.setJarByClass(WordCounterJob.class);
	job.setJobName("WordCount");
	FileInputFormat.addInputPath(job, new Path(args[0]));
	FileOutputFormat.setOutputPath(job, new Path(args[1]));
	//Speify the Mapper class
	job.setMapperClass(WordCounterMapper.class);
	//Specify the Reducer Class
	job.setReducerClass(WordCounterReducer.class);
	
	//Specify the output key of the mapper class
	job.setMapOutputKeyClass(Text.class);
	//Specify the output value of the mapper class
	job.setMapOutputValueClass(IntWritable.class);
	
	//specify the output key and value of reducer classs
	job.setOutputKeyClass(Text.class);
	job.setOutputValueClass(IntWritable.class);
	System.exit(job.waitForCompletion(true)? 0 :1);
	}

}