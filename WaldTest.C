#include <TH1.h>
#include <TF1.h>
#include <TH2.h>
#include <TTree.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TFitResult.h>
#include <TGraphErrors.h>


#include <string>
#include <vector>
#include <iostream>
#include <fstream>

void WaldTest()
{
	TH1F *hist = new TH1F("hist","SignalCount",6,0,5);
	//enum EBinErrorOpt;
	std::cout << "Bin uncertainties calculated based on " << hist->GetBinErrorOption() << std:: endl;
	hist->SetBinErrorOption(TH1::EBinErrorOpt(1));
	fstream file;
	file.open("DataFileWaldTest.txt",ios::in);

	int input;

	while(1)
	{
		file >> input;
		hist->Fill(input);
		if(file.eof()) break;
	}
	file.close();

	hist->GetXaxis()->SetTitle("EventType");
	hist->GetYaxis()->SetTitle("Counts");

	std::cout << "Now bin uncertainties calculated based on " << hist->GetBinErrorOption() << std:: endl;

	//for(unsigned int i=1; i < 7; i++)
	//{
	//	std::cout << "Bin Uncertainties for bin " << hist->GetBin(i) << " with " << hist->GetBinContent(i) << " counts are ( " << hist->GetBinErrorLow(i) << " , " << hist->GetBinErrorUp(i) << ") and as per Wald approximation is " << sqrt(hist->GetBinContent(i)) << std::endl;
	//}
	std::cout << "  N  " << "|" << "  Poisson  " << "|" <<  "  Wald  " << std::endl;
	std::cout << "-------------------------------------------------------" << std::endl;
	for(unsigned int i=1; i < 7; i++)
	{
		std::cout << hist->GetBinContent(i) << "  |  " << "+" << hist->GetBinErrorUp(i) << "-" << hist->GetBinErrorLow(i) << "   |   " << "+-" << sqrt(hist->GetBinContent(i)) << std::endl;
	}
	//printHistogram(hist);

	TCanvas *c1 = new TCanvas();
	hist->Draw();

}