# Narváez 

A locally hosted LLM chat application named after Luis Pacheco de Narváez, author of "Nueva Ciencia."

## Principals
1. Uses BASH terminals as the interface
1. Each terminal window will be a separate conversation
1. Conversations will not be stored by default
1. Build for maximum extensibility
    1. Microservice architecture
    1. YAML config files
1. Uses named agents for quickly identifying custom skill sets

## Structure
1. narvaez-core - LLM interaction / Conversation mgmt
1. narvaez-clean-doc - extract text from unstructured text documents
1. narvaez-cache - Redis caching
1. narvaez-storage - MongoDB storage
1. narvaez-graph - Graph DB Services

## Use
* General Q&A - Just ask a question
* Call expert - use @ notation to call a named expert

## Commands
### Conversation mgmt
* @save \<FILENAME> - saves current conversation to conversations directory
* @load \<FILENAME> - loads the specified conversation from the conversations directory
* @conversations - lists saved conversations
* @agents - lists contents of agent file
* @models - list available models
* @models \<MODELNAME> - force model use

### File storage and retrieval
* @cache \<FILENAME> - extracts text and uploads to redis for short term Q&A
* @save \<FILENAME> \<COLLECTION> - extracts text and saves file to long-term storage
* @extract \<FILENAME> - extracts text from file and uploads to Redis.  Returns Redis DB ID

## Config Files
* agent.yaml
  * name - expertise - prompt
* models.yaml
  * model_name - use
* config.yaml
  * conversations directory

## Needed Actions
* docker-build - ensure successful build of services
* super-lenter - code cleanup

