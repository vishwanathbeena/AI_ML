from preprocessing import docx_processing  as doc
from text_processing import tf_idf_cosine_similarity as tf_idf
from text_processing import cv_cosine_similarity as cv
import os
from nltk.stem.wordnet import WordNetLemmatizer


def process_files(req_document,resume_docs):
    req_doc_text = doc.get_content_as_string(req_document)
    resume_doc_text = []
    final_doc_rating_list = []
    for doct in resume_docs:
        resume_doc_text.append(doc.get_content_as_string(doct))
    #print('Req doc text is :')
    #print(req_doc_text)

    #print('Resume doc text is :')
    #print(resume_doc_text)
    # TF- cosine similarity
    cos_sim_list = tf_idf.get_tf_cosine_similarity(req_doc_text,resume_doc_text)

    zipped_docs = zip(cos_sim_list,resume_docs)
    sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    for element in sorted_doc_list:
        doc_rating_list = []
        doc_rating_list.append(os.path.basename(element[1]))
        doc_rating_list.append("{:.0%}".format(element[0]))
        final_doc_rating_list.append(doc_rating_list)
    # print('TF cosine similarity')
    # print(final_doc_rating_list)
    return final_doc_rating_list

    # TF-IDF - cosine similarity
    final_doc_rating_list = []
    cos_sim_list = tf_idf.get_tf_idf_cosine_similarity(req_doc_text,resume_doc_text)

    # zipped_docs = zip(cos_sim_list,resume_docs)
    # sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    # for element in sorted_doc_list:
    #     doc_rating_list = []
    #     doc_rating_list.append(os.path.basename(element[1]))
    #     doc_rating_list.append("{:.0%}".format(element[0]))
    #     final_doc_rating_list.append(doc_rating_list)
    # print('TF-IDF cosine similarity')
    # print(final_doc_rating_list)
    #
    # # binary cv - cosine similarity
    # final_doc_rating_list = []
    # cos_sim_list = cv.get_binay_cosine_similarity(req_doc_text,resume_doc_text)
    #
    # zipped_docs = zip(cos_sim_list,resume_docs)
    # sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    # for element in sorted_doc_list:
    #     doc_rating_list = []
    #     doc_rating_list.append(os.path.basename(element[1]))
    #     doc_rating_list.append("{:.0%}".format(element[0]))
    #     final_doc_rating_list.append(doc_rating_list)
    # print('Binary BOW cosine similarity')
    # print(final_doc_rating_list)
    #
    # # Regular cv - cosine similarity
    # final_doc_rating_list = []
    # cos_sim_list = cv.get_cosine_similarity(req_doc_text,resume_doc_text)
    #
    # zipped_docs = zip(cos_sim_list,resume_docs)
    # sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    # for element in sorted_doc_list:
    #     doc_rating_list = []
    #     doc_rating_list.append(os.path.basename(element[1]))
    #     doc_rating_list.append("{:.0%}".format(element[0]))
    #     final_doc_rating_list.append(doc_rating_list)
    # print(' BOW cosine similarity')
    # print(final_doc_rating_list)


# if __name__ == "__main__":
#     req_document = 'D:\\Learning\\test_word_docs\\JD\\WalletShare - P2 ETL DataStage JD.docx'
#     resume_docs = ['D:\\Learning\\test_word_docs\Resume\\Srinivas Sivadasu.docx',
#                    'D:\\Learning\\test_word_docs\Resume\\Pavan Reddy.docx',
#                    'D:\\Learning\\test_word_docs\Resume\\Veeranjaneyulu Tokala.docx']
#     # lemmatizer = WordNetLemmatizer()
#     # word_list = ['lead', 'leadership', 'leading']
#     # op = ' '.join(lemmatizer.lemmatize(w) for w in word_list)
#     # print(op)
#     process_files(req_document,resume_docs)






