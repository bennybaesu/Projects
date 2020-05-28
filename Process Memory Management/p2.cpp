#include <iostream>
#include <string>
#include <fstream>
#include <queue>
using namespace std;


    struct Process
    {
        int id, arrivalTime, lifetime, addressSpace, turnaroundTime;
        bool complete;
    };

void removeProcess(Process p, int page[], int page_size, int pageChunks, int n);
void printMemMap (int page[], int page_size, int pageChunks, int n);
void addProcess(Process p, int page[], int page_size, int pageChunks, int n);
void showq(queue <int> a)
{
    queue <int> b = a;
    while(!b.empty())
    {
        cout << " " << b.front();
        b.pop();
    }
}



void memMap(Process p, int page[]);


int main()
{
    // DECLARATIONS*****************************************************
    int memory_size = 0;
    int page_size = 0;
    int maxMem = 0;
    int currentMem = 0;
    string fileName = " ";
    bool validFile = true;
    int n = 0;
    int clock = 0;
    queue <int> inputQueue;
    queue <int> mem;
    queue <int> temp;
    int size = 0;
    int memCounter = 0;
    bool ended = false;
    bool changeDetected = false;
    bool clockChange = false;
    int pageChunks = 0;

    

    // ****************************************************************
    

    // GET THE MEMORY SIZE FROM THE USER*******************************
    do
    {
        cout << "Enter memory size: ";
        cin >> memory_size;
        
        if(memory_size <= 0)
        {
            cout << "Memory size entered is too small. Try again\n";
            cin.clear();
        }
        
        if(memory_size >= 10000)
        {
            cout << "That memory size is too large. Try again.\n";
            cin.clear();
        }
        
    } while (memory_size <= 0 || memory_size >= 100000);
    
    maxMem = memory_size;
    currentMem = maxMem;
    // ****************************************************************
    
    
    // GET THE PAGE SIZE FROM THE USER*********************************
    do
    {
		cout << "Page numbers:" << endl;
        cout << "1: 100\n2: 200\n3:400" << endl;
        cout << "Enter an option (1, 2, 3): ";
        cin >> page_size;
        
        if(page_size != 1 && page_size != 2 && page_size != 3)
        {
            cout << "That is not a valid option. Try again.\n";
            cin.clear();
        }
    } while (page_size != 1 && page_size != 2 && page_size != 3);
    if(page_size == 1)
        page_size = 100;
    if(page_size == 2)
        page_size = 200;
    if(page_size == 3)
        page_size = 400;
    pageChunks = memory_size / page_size;
    int* page = new int [pageChunks];
    for(int i = 0; i < pageChunks; i++)
    {
        page[i] = 0;
    }
    // ****************************************************************
    
    
    // GET THE WORKLOAD FILE NAME FROM THE USER ***********************
    ifstream file;
    do
     {
        cout << "Enter name of workload file: ";
        cin >> fileName;
        file.open(fileName);
        if(file.fail())
        {
            cout << "File is invalid. Try using the full file path." << endl;
            validFile = false;
            cin.clear();
        }
        else
        validFile = true;
    } while(!validFile);
    // /home/bennybaesu/Downloads/in1.txt
    
    // ****************************************************************


    // PUT FILE COMPONENTS INTO ARRAYS*********************************
    file >> n;                        // Number of processes in 'in.txt'
    Process *p = new Process[n];
    
    int j = 0;                        // Number of address space components
    
    int adder = 0;
    for(int i = 0; i < n; i++)
    {
        file >> p[i].id;
        file >> p[i].arrivalTime;
        file >> p[i].lifetime;
        p[i].addressSpace = 0;
        file >> j;
        for(int k = 0; k < j; k++)
        {
            file >> adder;
            p[i].addressSpace += adder;
        }
        
        
        
    }
    file.close();
    // ****************************************************************
    
    
    
    // MEMORY MANAGEMENT BEGINS***************************************
    bool timeDisplay = false;
    while(clock <= 100000)
    {
        //cout << "t = " << clock << ":\n";
        clockChange = true;
        timeDisplay = false;
        do
        {
            changeDetected = false;
            
            // Add all processes to the queue that arrive now
            for(int i = 0; i < n; i++)
            {
                if(p[i].arrivalTime == clock && clockChange)
                {
					if(!changeDetected && !timeDisplay)
					{
						cout << "t = " << clock << ":\n";
						timeDisplay = true;
						
					}
                    cout << "\t\tProcess " << p[i].id << " arrives.\n\t";
                    inputQueue.push(p[i].id);
                    cout << "\t\tInput queue: [";
                    showq(inputQueue);
                    cout << " ]\n";
                }
            }
            
            // Update all processes for where they're at
            if(!mem.empty())
            {
                temp = mem;
                size = mem.size();
            
                for(int i = 0; i < size; i++)
                {
                    if(clockChange)
                    {
                        p[temp.front()-1].lifetime -= 100;

                    }
                    temp.pop();
                }
            }
        
        
            // Remove all processes from memory that are finished
            while(!mem.empty())
            {
                if(p[mem.front() - 1].lifetime > 0)
                {
                    temp.push(mem.front());
                    mem.pop();
                }
                else
                {
                    currentMem += p[mem.front() - 1].addressSpace;
                    if(currentMem > maxMem)
                    {
                        currentMem = maxMem;
                    }
                    if(!changeDetected && !timeDisplay)
					{
						cout << "t = " << clock << ":\n";
						timeDisplay = true;
						
					}
                    cout << "\t\tProcess " << p[mem.front() - 1].id;
                    cout << " completes.\n";
					removeProcess(p[mem.front() - 1], page, page_size, pageChunks, n);
					p[mem.front() - 1].turnaroundTime = clock - p[mem.front() - 1].arrivalTime;
                    mem.pop();
                    memCounter++;
                    changeDetected = true;
                    
                }
                
                
                if(mem.empty() && inputQueue.empty() && memCounter == n)
                    {
						if(!changeDetected && !timeDisplay)
					{
						cout << "t = " << clock << ":\n";
						timeDisplay = true;
						
					}
                        cout << "All processes completed.\n";
                        ended = true;
                    }
            }
            if (ended)
            {
                clock = 100000;
                break;
            }
            
            
            mem = temp;
        
	int mod = 0;
	Process temp;
	int chunkCounter = 0;
        int requiredChunks = 0;
            // Add all processes to main memory from the queue that can be handled
            if(!inputQueue.empty())
            {    size = inputQueue.size();
                for(int i = 0; i < size; i++)
                {
					temp = p[(inputQueue.front()) - 1];
					if(temp.addressSpace % page_size != 0)
					{
						mod = temp.addressSpace % page_size;
						mod = page_size - mod;
						temp.addressSpace += mod;
					}
					requiredChunks = temp.addressSpace / page_size;
					for(int j = 0; j < pageChunks; j++)
					{
						if(page[j] == 0)
						{
							chunkCounter++;
						}
					}
					
                    if(requiredChunks <= chunkCounter)
                    {
                        mem.push(inputQueue.front());
                        currentMem -= p[inputQueue.front() - 1].addressSpace;
                        cout << "\t\tMM moves Process " << p[inputQueue.front() - 1].id;
                        cout << " to memory.\n";
                        addProcess(p[inputQueue.front() -1], page, page_size, pageChunks, n);
                        inputQueue.pop();
                        cout << "\t\tInput queue: [";
                        showq(inputQueue);
                        cout << " ]\n";
                        changeDetected = true;
                        
                    }
            
                }
            }
            clockChange = false;     
        } while( changeDetected);
        clock += 100;
    }
    
    if(clock == 100000)
    {
        cout << "Clock has reached 100,000. Time has run out." << endl;
	}
        
        int average = 0;
        for(int i = 0; i < n; i++)
        {
			average += p[i].turnaroundTime;
		}
		average = average / n;
		
		cout << "\nAverage Turnaround Time: " << average << endl;

    
    
    
    
    
    
    delete [] p;
    delete [] page;
    return 0;
}


void addProcess(Process p, int page[], int page_size, int pageChunks, int n)
{
	int mod = 0;
	if(p.addressSpace % page_size != 0)
        {
			mod = p.addressSpace % page_size;
			mod = page_size - mod;
			p.addressSpace += mod;
		}
		
		
	int stop = p.addressSpace;
	int counter = 0;
	for (int i = 0; i < pageChunks; i++)
	{ 
		if (counter >= stop)
		break;
		if (page[i] == 0)
		{
			page[i] = p.id;
			counter+= page_size;
			
		}
	}
	printMemMap(page, page_size, pageChunks, n);   
}


void removeProcess(Process p, int page[], int page_size, int pageChunks, int n)
{
    for (int i = 0; i < pageChunks; i++)
    {
    if (page[i] == p.id)
        {
        page[i] = 0;
}
    }
printMemMap(page, page_size, pageChunks, n);
}



void printMemMap (int page[], int page_size, int pageChunks, int n)
{
    int counter[pageChunks];
    for(int i = 0; i < pageChunks; i++)
{
        counter[i] = 0;
}

    cout << "\t\tMemory Map:\n";

    for (int i = 0; i < pageChunks; i++)
    {
        
        if (page[i] == 0)
        {
			if(page[i-1] != 0 || i == 0)
			{
				cout << "\t\t\t" << (page_size*i) << "-";
			}
			if(page[i+1] != 0 || i == pageChunks - 1)
			{
				cout << ((page_size * (i+1)) - 1) << ": ";
				cout << "Free frame(s)" << endl;
			}
        }  
        else
        {    
			cout << "\t\t\t" << (page_size*i) << "-" << ((page_size * (i+1)) - 1) << ": ";
			counter[page[i]]++;
            cout << "Process " << page[i] << ", Page " << counter[page[i]] << endl;
        }
        }
}

